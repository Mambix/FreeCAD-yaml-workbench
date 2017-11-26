import os
import FreeCAD as App, Mesh
from yaml import load

if App.GuiUp:
    import FreeCADGui as Gui

if open.__module__ == '__builtin__': pythonopen = open

predefined_colors = {
    'red': (1.0, 0.0, 0.0),
    'darkGed': (0.67, 0.0, 0.0),
    'green': (0.0, 1.0, 0.0),
    'darkGreen': (0.0, 0.67, 0.0),
    'blue': (0.0, 0.0, 1.0),
    'darkBlue': (0.0, 0.0, 0.67),
    'yellow': (1.0, 1.0, 0.0),
    'cyan': (0.0, 1.0, 1.0),
    'purple': (1.0, 0.0, 1.0),
    'white': (1.0, 1.0, 1.0),
    'lightGray': (0.75, 0.75, 0.75),
    'gray': (0.5, 0.5, 0.5),
    'darkGray': (0.25, 0.25, 0.25),
}

def open(filename):
    base_directory = os.path.dirname(filename)
    sub_directory = None
    print('Reading: {}'.format(filename))
    print('Base: {}'.format(base_directory))

    yaml_data = None
    with pythonopen(filename, 'r') as f:
        yaml_data = load(f)

    if yaml_data is None:
        raise Exception("Error reading YAML file: {}".format(filename))

    print('YML data: {}'.format(yaml_data))
    if 'settings' in yaml_data:
        if 'subDirectory' in yaml_data['settings']:
            base_directory += '/{}'.format(yaml_data['settings']['subDirectory'])
            print('Base: {}'.format(base_directory))

    if 'import' not in yaml_data:
        raise Exception('No \'import\' section in YAML file!!!')

    yaml_data = yaml_data['import']

    for document, document_data in yaml_data.iteritems():
        doc = App.newDocument(document)

        for group, group_data in document_data.iteritems():
            App.getDocument(document).addObject("App::DocumentObjectGroup", group)

            if isinstance(group_data, basestring):
                Mesh.insert(u'{}/{}'.format(base_directory, group_data), document)
                continue

            if isinstance(group_data, list):
                for file in group_data:
                    Mesh.insert(u'{}/{}'.format(base_directory, file), document)
                continue

            for file, file_data in group_data.iteritems():
                if file == 'files':
                    for f in file_data:
                        Mesh.insert(u'{}/{}'.format(base_directory, f), document)
                    continue
                Mesh.insert(u'{}/{}'.format(base_directory, file), document)
                if 'color' in file_data:
                    color_data = file_data['color']
                    shape_color = None
                    if not isinstance(color_data, list):
                        if color_data not in predefined_colors:
                            raise Exception('Color data needs to be an array of RGB floats or one of predefined colors!!!')
                        shape_color = predefined_colors[color_data]
                    else:
                        shape_color = (color_data[0], color_data[1], color_data[2])
                    Gui.getDocument(document).getObject(file[:-4]).ShapeColor = shape_color

        doc.recompute()

    Gui.activeDocument().activeView().viewAxonometric()
    Gui.SendMsgToActiveView("ViewFit")

import os
import FreeCAD as App, Mesh
from yaml import load

if App.GuiUp:
    import FreeCADGui as Gui

if open.__module__ == '__builtin__': pythonopen = open

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
                Mesh.insert(u'{}/{}'.format(base_directory, file), document)

        doc.recompute()

    Gui.SendMsgToActiveView("ViewFit")

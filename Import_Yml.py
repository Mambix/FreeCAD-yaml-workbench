import os
import sys
import FreeCAD as App, Mesh
from yaml import load

if App.GuiUp:
    import FreeCADGui as Gui


if not sys.version_info.major == 3:
    print("This script requires Python 3.x")
    print("You are using Python {}.{}.".format(sys.version_info.major, sys.version_info.minor))
    sys.exit(1)

pythonopen = open
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


def insertMesh(directory, filename, document, document_name, group, attributes = None):
    Mesh.insert(u'{}/{}'.format(directory, filename), document_name)
    new_mesh = document.getObject(filename[:-4])
    if attributes:
        color = getColor(attributes)
        if color:
            new_mesh.ViewObject.ShapeColor = color
        transparency = getTransparency(attributes)
        if transparency:
            new_mesh.ViewObject.Transparency = transparency
        placement = getPlacement(attributes)
        rotation = getRotation(attributes)
        new_mesh.Placement = App.Placement(placement, rotation)
    group.addObject(new_mesh)

def getColor(json_data):
    color_data = json_data.get('color', None)
    if not color_data:
        return None
    if not isinstance(color_data, list):
        if color_data not in predefined_colors:
            raise Exception('Color data needs to be an array of RGB floats or one of predefined colors!!!')
        return predefined_colors[color_data]
    return (color_data[0], color_data[1], color_data[2])

def getTransparency(json_data):
    return json_data.get('transparency', None)

def getPlacement(json_data):
    placement = App.Vector(.0, .0, .0)
    placement_config = json_data.get('placement', None)
    if placement_config:
        placement = App.Vector(*placement_config)
    return placement

def getRotation(json_data):
    rotation_vector = json_data.get('rotationVector', (.0, .0, 1.0))
    rotation_angle = json_data.get('rotationAngle', 0.0)
    return App.Rotation(App.Vector(*rotation_vector), rotation_angle)

def open(filename):
    base_directory = os.path.dirname(filename)
    sub_directory = None
    print('Reading: {}'.format(filename))
    print('Base: {}'.format(base_directory))

    yaml_data = None
    with pythonopen(filename) as f:
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

    for document_name, document_data in yaml_data.items():
        document = App.newDocument(document_name)

        for group_name, group_data in document_data.items():
            document_group = document.addObject("App::DocumentObjectGroup", group_name)

            if isinstance(group_data, str):
                insertMesh(base_directory, group_data, document, document_name, document_group)
                continue

            if isinstance(group_data, list):
                for file in group_data:
                    insertMesh(base_directory, file, document, document_name, document_group)
                continue

            for file, file_data in group_data.items():
                if file == 'files':
                    for f in file_data:
                        insertMesh(base_directory, f, document, document_name, document_group)
                    continue
                insertMesh(base_directory, file, document, document_name, document_group, file_data)
        document.recompute()
    Gui.activeDocument().activeView().viewAxonometric()
    Gui.SendMsgToActiveView("ViewFit")

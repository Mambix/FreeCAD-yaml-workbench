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


def insertMesh(directory, filename, document, group, attributes = None):
    mesh = Mesh.Mesh(u'{}/{}'.format(directory, filename))
    object_name = filename[:-4]
    if 'objectName' in attributes:
        object_name = attributes['objectName']
    new_mesh = document.addObject("Mesh::Feature", object_name)
    new_mesh.Mesh = mesh
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

def insertSolid(name, document, group, attributes):
    if attributes['solid'] == 'cylinder':
        return insertCylinder(name, document, group, attributes)
    print('ERROR: Unsupported solid tyle {}'.format(attributes['solid']))

def insertCylinder(name, document, group, attributes):
    solid = document.addObject("Part::Cylinder","Cylinder")
    solid.Label = name
    solid.Radius = '{} mm'.format(attributes['radius'])
    solid.Height = '{} mm'.format(attributes['height'])
    if 'angle' in attributes:
        solid.Angle = '{} deg'.format(attributes['angle'])
    color = getColor(attributes)
    if color:
        solid.ViewObject.ShapeColor = color
    transparency = getTransparency(attributes)
    if transparency:
        solid.ViewObject.Transparency = transparency
    placement = getPlacement(attributes)
    rotation = getRotation(attributes)
    solid.Placement = App.Placement(placement, rotation)
    group.addObject(solid)

def insertSphere(name, document, group, attributes):
    solid = document.addObject("Part::Sphere","Sphere")
    solid.Label = name
    solid.Radius = '{} mm'.format(attributes['radius'])
    if 'angle1' in attributes:
        solid.Angle1 = '{} deg'.format(attributes['angle1'])
    if 'angle2' in attributes:
        solid.Angle2 = '{} deg'.format(attributes['angle2'])
    if 'angle3' in attributes:
        solid.Angle3 = '{} deg'.format(attributes['angle3'])
    color = getColor(attributes)
    if color:
        solid.ViewObject.ShapeColor = color
    transparency = getTransparency(attributes)
    if transparency:
        solid.ViewObject.Transparency = transparency
    placement = getPlacement(attributes)
    rotation = getRotation(attributes)
    solid.Placement = App.Placement(placement, rotation)
    group.addObject(solid)

def insertEllipsoid(name, document, group, attributes):
    solid = document.addObject("Part::Ellipsoid","Ellipsoid")
    solid.Label = name
    solid.Radius1 = '{} mm'.format(attributes['radius1'])
    solid.Radius2 = '{} mm'.format(attributes['radius2'])
    solid.Radius3 = '{} mm'.format(attributes['radius3'])
    if 'angle1' in attributes:
        solid.Angle1 = '{} deg'.format(attributes['angle1'])
    if 'angle2' in attributes:
        solid.Angle2 = '{} deg'.format(attributes['angle2'])
    if 'angle3' in attributes:
        solid.Angle3 = '{} deg'.format(attributes['angle3'])
    color = getColor(attributes)
    if color:
        solid.ViewObject.ShapeColor = color
    transparency = getTransparency(attributes)
    if transparency:
        solid.ViewObject.Transparency = transparency
    placement = getPlacement(attributes)
    rotation = getRotation(attributes)
    solid.Placement = App.Placement(placement, rotation)
    group.addObject(solid)

def insertBox(name, document, group, attributes):
    solid = document.addObject("Part::Box","Box")
    solid.Label = name
    solid.Length = '{} mm'.format(attributes['length'])
    solid.Width = '{} mm'.format(attributes['width'])
    solid.Height = '{} mm'.format(attributes['height'])
    color = getColor(attributes)
    if color:
        solid.ViewObject.ShapeColor = color
    transparency = getTransparency(attributes)
    if transparency:
        solid.ViewObject.Transparency = transparency
    placement = getPlacement(attributes)
    rotation = getRotation(attributes)
    solid.Placement = App.Placement(placement, rotation)
    group.addObject(solid)

def insertCone(name, document, group, attributes):
    solid = document.addObject("Part::Cone","Cone")
    solid.Label = name
    solid.Radius1 = '{} mm'.format(attributes['radius1'])
    solid.Radius2 = '{} mm'.format(attributes['radius2'])
    solid.Height = '{} mm'.format(attributes['height'])
    if 'angle' in attributes:
        solid.Angle = '{} deg'.format(attributes['angle'])
    color = getColor(attributes)
    if color:
        solid.ViewObject.ShapeColor = color
    transparency = getTransparency(attributes)
    if transparency:
        solid.ViewObject.Transparency = transparency
    placement = getPlacement(attributes)
    rotation = getRotation(attributes)
    solid.Placement = App.Placement(placement, rotation)
    group.addObject(solid)

def insertTorus(name, document, group, attributes):
    solid = document.addObject("Part::Torus","Torus")
    solid.Label = name
    solid.Radius1 = '{} mm'.format(attributes['radius1'])
    solid.Radius2 = '{} mm'.format(attributes['radius2'])
    if 'angle1' in attributes:
        solid.Angle1 = '{} deg'.format(attributes['angle1'])
    if 'angle2' in attributes:
        solid.Angle2 = '{} deg'.format(attributes['angle2'])
    if 'angle3' in attributes:
        solid.Angle3 = '{} deg'.format(attributes['angle3'])
    color = getColor(attributes)
    if color:
        solid.ViewObject.ShapeColor = color
    transparency = getTransparency(attributes)
    if transparency:
        solid.ViewObject.Transparency = transparency
    placement = getPlacement(attributes)
    rotation = getRotation(attributes)
    solid.Placement = App.Placement(placement, rotation)
    group.addObject(solid)

def insertPrism(name, document, group, attributes):
    solid = document.addObject("Part::Prism","Prism")
    solid.Label = name
    solid.Polygon = '{}'.format(attributes['polygon'])
    solid.Circumradius = '{} mm'.format(attributes['radius'])
    solid.Height = '{} mm'.format(attributes['Height'])
    color = getColor(attributes)
    if color:
        solid.ViewObject.ShapeColor = color
    transparency = getTransparency(attributes)
    if transparency:
        solid.ViewObject.Transparency = transparency
    placement = getPlacement(attributes)
    rotation = getRotation(attributes)
    solid.Placement = App.Placement(placement, rotation)
    group.addObject(solid)

def insertWedge(name, document, group, attributes):
    solid = document.addObject("Part::Wedge","Wedge")
    solid.Label = name
    solid.Xmin = '{} mm'.format(attributes['xmin'])
    solid.Ymin = '{} mm'.format(attributes['ymin'])
    solid.Zmin = '{} mm'.format(attributes['zmin'])
    solid.X2min = '{} mm'.format(attributes['x2min'])
    solid.Z2min = '{} mm'.format(attributes['z2min'])
    solid.Xmax = '{} mm'.format(attributes['xmax'])
    solid.Ymax = '{} mm'.format(attributes['ymax'])
    solid.Zmax = '{} mm'.format(attributes['zmax'])
    solid.X2max = '{} mm'.format(attributes['x2max'])
    solid.Z2max = '{} mm'.format(attributes['z2max'])
    color = getColor(attributes)
    if color:
        solid.ViewObject.ShapeColor = color
    transparency = getTransparency(attributes)
    if transparency:
        solid.ViewObject.Transparency = transparency
    placement = getPlacement(attributes)
    rotation = getRotation(attributes)
    solid.Placement = App.Placement(placement, rotation)
    group.addObject(solid)

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
                insertMesh(base_directory, group_data, document, document_group)
                continue

            if isinstance(group_data, list):
                for file in group_data:
                    insertMesh(base_directory, file, document, document_group)
                continue

            for file, file_data in group_data.items():
                if file == 'files':
                    for f in file_data:
                        insertMesh(base_directory, f, document, document_group)
                    continue
                if not isinstance(file_data, list):
                    if 'solid' not in file_data:
                        insertMesh(base_directory, file, document, document_group, file_data)
                    else:
                        insertSolid(file, document, document_group, file_data)
                else:
                    for file_data2 in file_data:
                        insertMesh(base_directory, file, document, document_group, file_data2)
        document.recompute()
    Gui.activeDocument().activeView().viewAxonometric()
    Gui.SendMsgToActiveView("ViewFit")


import FreeCAD as App , Mesh , Part

from builtins import open as openFile
from Colors import Colors
from yaml import safe_load
from sys import version_info as version , exit
from os import path


if App.GuiUp:
    import FreeCADGui as Gui

if not version.major == 3:
    print('This script requires Python 3.x')
    print(f'You are using Python { version.major }.{ version.minor }')
    exit(1)


def insertObject(directory, filename, document, group, attributes = None):
    if not path.isfile(path.join(directory, filename)):
        directory = path.expanduser('~/.FreeCAD/Mod/yaml-workspace')
        if not path.isfile(path.join(directory, filename)):
            print(f'ERROR: `{ filename }` not found!')
            return
    if filename[-4:] in ['.stp', '.igs', 'iges', 'step']:
        return insertPart(directory, filename, document, group, attributes)
    insertMesh(directory, filename, document, group, attributes)

def insertMesh(directory, filename, document, group, attributes = None):
    mesh = Mesh.Mesh(path.join(directory,filename))
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

def insertPart(directory, filename, document, group, attributes = None):
    if not path.isfile(path.join(directory, filename)):
        directory = path.expanduser('~/.FreeCAD/Mod/yaml-workspace')
        if not path.isfile(path.join(directory, filename)):
            print(f'ERROR: `{ filename }` not found!')
            return

    part = Part.Shape()
    part = Part.read(path.join(directory,filename))
    object_name = filename[:-4]
    if 'objectName' in attributes:
        object_name = attributes['objectName']
    new_part = document.addObject("Part::Feature", object_name)
    new_part.Shape = part
    if attributes:
        color = getColor(attributes)
        if color:
            new_part.ViewObject.ShapeColor = color
        transparency = getTransparency(attributes)
        if transparency:
            new_part.ViewObject.Transparency = transparency
        placement = getPlacement(attributes)
        rotation = getRotation(attributes)
        new_part.Placement = App.Placement(placement, rotation)
    group.addObject(new_part)

def insertCylinder(name, document, group, attributes):
    solid = document.addObject("Part::Cylinder","Cylinder")
    solid.Label = name
    solid.Radius = f'{ attributes[ "radius" ] } mm'
    solid.Height = f'{ attributes[ "height" ] } mm'
    if 'angle' in attributes:
        solid.Angle = f'{ attributes[ "angle" ] } deg'
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
    solid.Radius = f'{ attributes[ "radius" ] } mm'
    if 'angle1' in attributes:
        solid.Angle1 = f'{ attributes[ "angle1" ] } deg'
    if 'angle2' in attributes:
        solid.Angle2 = f'{ attributes[ "angle2" ] } deg'
    if 'angle3' in attributes:
        solid.Angle3 = f'{ attributes[ "angle3" ] } deg'
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
    solid.Radius1 = f'{ attributes[ "radius1" ] } mm'
    solid.Radius2 = f'{ attributes[ "radius2" ] } mm'
    solid.Radius3 = f'{ attributes[ "radius3" ] } mm'
    if 'angle1' in attributes:
        solid.Angle1 = f'{ attributes[ "angle1" ] } deg'
    if 'angle2' in attributes:
        solid.Angle2 = f'{ attributes[ "angle2" ] } deg'
    if 'angle3' in attributes:
        solid.Angle3 = f'{ attributes[ "angle3" ] } deg'
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
    solid.Length = f'{ attributes[ "length" ] } mm'
    solid.Height = f'{ attributes[ "height" ] } mm'
    solid.Width = f'{ attributes[ "width" ] } mm'
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
    solid.Radius1 = f'{ attributes[ "radius1" ] } mm'
    solid.Radius2 = f'{ attributes[ "radius2" ] } mm'
    solid.Height = f'{ attributes[ "height" ] } mm'
    if 'angle' in attributes:
        solid.Angle = f'{ attributes[ "angle" ] } deg'
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
    solid.Radius1 = f'{ attributes[ "radius1" ] } mm'
    solid.Radius2 = f'{ attributes[ "radius2" ] } mm'
    if 'angle1' in attributes:
        solid.Angle1 = f'{ attributes[ "angle1" ] } deg'
    if 'angle2' in attributes:
        solid.Angle2 = f'{ attributes[ "angle2" ] } deg'
    if 'angle3' in attributes:
        solid.Angle3 = f'{ attributes[ "angle3" ] } deg'
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
    solid.Polygon = int(attributes[ "polygon" ])
    solid.Circumradius = f'{ attributes[ "radius" ] } mm'
    solid.Height = f'{ attributes[ "height" ] } mm'
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
    solid.Xmin = f'{ attributes[ "xmin" ] } mm'
    solid.Ymin = f'{ attributes[ "ymin" ] } mm'
    solid.Zmin = f'{ attributes[ "zmin" ] } mm'
    solid.X2min = f'{ attributes[ "x2min" ] } mm'
    solid.Z2min = f'{ attributes[ "z2min" ] } mm'
    solid.Xmax = f'{ attributes[ "xmax" ] } mm'
    solid.Ymax = f'{ attributes[ "ymax" ] } mm'
    solid.Zmax = f'{ attributes[ "zmax" ] } mm'
    solid.X2max = f'{ attributes[ "x2max" ] } mm'
    solid.Z2max = f'{ attributes[ "z2max" ] } mm'
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

def getColor ( data ):

    color = data.get('color', None)
    
    if not color:
        return None
    
    if isinstance(color,list):
        return ( color[0] , color[1] , color[2] )

    if color in Colors:
        return Colors[ color ]
    
    raise Exception('Color data needs to be an array of RGB floats or one of predefined colors!')
    

def getTransparency(json_data):
    return json_data.get('transparency', None)

def getPlacement ( data ):
    
    config = data.get('placement',None)
    
    if config:
        return App.Vector(*config)
        
    return App.Vector(0.0,0.0,0.0)


def getRotation ( data ):

    points = data.get('rotationVector',(0.0,0.0,1.0))
    angle = data.get('rotationAngle',0.0)

    vector = App.Vector(*points)

    return App.Rotation(vector,angle)


Shapes = {
    'ellipsoid' : insertEllipsoid ,
    'cylinder' : insertCylinder ,
    'sphere' : insertSphere ,
    'wedge' : insertWedge ,
    'torus' : insertTorus ,
    'prism' : insertPrism ,
    'cone' : insertCone ,
    'box' : insertBox
}


def insertSolid ( name , document , group , attributes ):
    
    type = attributes[ "solid" ]

    if type in Shapes:
        return Shapes[ type ](name,document,group,attributes)

    print(f'ERROR: Unsupported solid type { type }')


def open(filename):
    base_directory = path.dirname(filename)
    print(f'Reading: { filename }')
    print(f'Base: { base_directory }')

    yaml_data = None
    with openFile(filename) as f:
        yaml_data = safe_load(f)

    if yaml_data is None:
        raise Exception(f'Error reading YAML file: { filename }')

    print(f'YML data: { yaml_data }')
    if 'settings' in yaml_data:
        if 'subDirectory' in yaml_data[ "settings" ]:
            
            folder = yaml_data[ 'settings' ][ 'subDirectory' ]

            base_directory = path.join(base_directory,folder)

            print(f'Base: { base_directory }')

    if 'import' not in yaml_data:
        raise Exception('No \'import\' section in YAML file!!!')

    yaml_data = yaml_data['import']

    for document_name, document_data in yaml_data.items():
        document = App.newDocument(document_name)

        for group_name, group_data in document_data.items():
            document_group = document.addObject("App::DocumentObjectGroup", group_name)

            if isinstance(group_data, str):
                insertObject(base_directory, group_data, document, document_group)
                continue

            if isinstance(group_data, list):
                for file in group_data:
                    insertObject(base_directory, file, document, document_group)
                continue

            for file, file_data in group_data.items():
                if file == 'files':
                    for f in file_data:
                        insertObject(base_directory, f, document, document_group)
                    continue
                if not isinstance(file_data, list):
                    if 'solid' not in file_data:
                        insertObject(base_directory, file, document, document_group, file_data)
                    else:
                        insertSolid(file, document, document_group, file_data)
                else:
                    for file_data2 in file_data:
                        insertObject(base_directory, file, document, document_group, file_data2)
        document.recompute()
    Gui.activeDocument().activeView().viewAxonometric()
    Gui.SendMsgToActiveView("ViewFit")

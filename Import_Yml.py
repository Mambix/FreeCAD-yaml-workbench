
from Source.Objects.Base import defineBasics
from Source.Objects import *
from builtins import open as openFile
from FreeCAD import newDocument , GuiUp
from yaml import safe_load
from os import path


if GuiUp:
    import FreeCADGui as Gui # type: ignore

def insertObject(directory, filename, document, group, attributes = None):
    if not path.isfile(path.join(directory, filename)):
        directory = path.expanduser('~/.FreeCAD/Mod/yaml-workspace')
        if not path.isfile(path.join(directory, filename)):
            print(f'ERROR: `{ filename }` not found!')
            return
    if filename[-4:] in ['.stp', '.igs', 'iges', 'step']:
        return insertPart(directory, filename, document, group, attributes)
    insertMesh(directory, filename, document, group, attributes)



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

    if not type in Shapes:
        print(f'ERROR: Unsupported solid type { type }')
        return
    
    shape = Shapes[ type ](document,attributes)
    shape.Label = name

    defineBasics(shape,attributes)

    group.addObject(shape)


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
        document = newDocument(document_name)

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

    Gui.activeDocument().activeView().viewAxonometric() # type: ignore
    Gui.SendMsgToActiveView("ViewFit") # type: ignore

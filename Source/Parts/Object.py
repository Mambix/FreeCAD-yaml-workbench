
from Source.Parts.Mesh import insertMesh
from Source.Parts.Part import insertPart
from os import path


def insertObject(directory, filename, document, group, attributes = None):
    if not path.isfile(path.join(directory, filename)):
        directory = path.expanduser('~/.FreeCAD/Mod/yaml-workspace')
        if not path.isfile(path.join(directory, filename)):
            print(f'ERROR: `{ filename }` not found!')
            return
    if filename[-4:] in ['.stp', '.igs', 'iges', 'step']:
        return insertPart(directory, filename, document, group, attributes)
    insertMesh(directory, filename, document, group, attributes)
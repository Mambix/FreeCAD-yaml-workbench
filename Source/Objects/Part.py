
from Source.Objects.Base import defineBasics
from Part import Shape , read
from os import path


def insertPart(directory, filename, document, group, attributes : dict | None = None):
    if not path.isfile(path.join(directory, filename)):
        directory = path.expanduser('~/.FreeCAD/Mod/yaml-workspace')
        if not path.isfile(path.join(directory, filename)):
            print(f'ERROR: `{ filename }` not found!')
            return

    part = Shape()
    part = read(path.join(directory,filename))
    object_name = filename[:-4]
    
    if attributes:
        if 'objectName' in attributes:
            object_name = attributes['objectName']
    
    new_part = document.addObject("Part::Feature", object_name)
    new_part.Shape = part

    if attributes:
        defineBasics(new_part,attributes)

    group.addObject(new_part)

from Source.Parts.Common import defineCommon
from os.path import expanduser , isfile , join
from Part import Shape , read


def insertPart ( directory , filename , document , group , attributes : dict | None = None ):

    path = join(directory,filename)

    if not isfile(path):

        directory = expanduser('~/.FreeCAD/Mod/yaml-workspace')

        path = join(directory,filename)

        if not isfile(path):
            print(f'ERROR: `{ filename }` not found!')
            return

    shape = Shape()
    shape = read(path)

    name = filename[:-4]
    
    if attributes:
        if 'objectName' in attributes:
            name = attributes[ 'objectName' ]
    
    part = document.addObject('Part::Feature',name)
    part.Shape = shape

    if attributes:
        defineCommon(part,attributes)

    group.addObject(part)
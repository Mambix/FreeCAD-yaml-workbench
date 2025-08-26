
from .Common import defineCommon
from os.path import expanduser , isfile , join
from Part import Shape , read


def insertPart ( folder , file , document , group , data : dict | None = None ):

    path = join(folder,file)

    if not isfile(path):
        folder = expanduser('~/.FreeCAD/Mod/yaml-workspace')

    path = join(folder,file)

    if not isfile(path):
        print(f'''ERROR: '{ file }' not found!''')
        return

    shape = Shape()
    shape = read(path)

    name = file[:-4]
    
    if data:
        if 'objectName' in data:
            name = data[ 'objectName' ]
    
    object = document.addObject('Part::Feature',name)
    object.Shape = shape

    if data:
        defineCommon(object,data)

    group.addObject(object)
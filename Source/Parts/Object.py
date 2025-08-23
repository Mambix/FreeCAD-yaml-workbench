
from Source.Parts.Mesh import insertMesh
from Source.Parts.Part import insertPart
from os.path import expanduser , isfile , join


Part_Extensions = [ '.stp', '.igs', 'iges', 'step' ]


def insertObject ( folder , file , document , group , data = None ):

    path = join(folder,file)

    if not isfile(path):
    
        folder = expanduser('~/.FreeCAD/Mod/yaml-workspace')
    
    path = join(folder,file)

    if not isfile(path):
        print(f'''ERROR: '{ file }' not found!''')
        return
    
    if file[-4:] in Part_Extensions:
        insertPart(folder,file,document,group,data)
    else:
        insertMesh(folder,file,document,group,data)
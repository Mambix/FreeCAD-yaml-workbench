
from ..Crypto import hash
from requests import get as fetch
from os.path import expanduser , isfile , join
from .Mesh import insertMesh
from .Part import insertPart


Part_Extensions = [ '.stp', '.igs', 'iges', 'step' ]


def insertObject ( document , group , folder , file , data : dict | None = None ):

    extension = file[-4:]

    if extension[0] == '.':
        extension = extension[1:]

    if folder[0:4] == 'http':

        url = join(folder,file)

        file = f'{ hash(url) }.{ extension }'

        folder = expanduser('~/.FreeCAD/Mod/yaml-workspace')

        path = join(folder,file)
        
        if not isfile(path):

            print(f'Fetching object from \'{ url }\'')

            response = fetch(url, stream = True )
            
            if not response.ok:
                print(f'ERROR: `{ url }` not found!')
                return

            with open(path,'wb+') as f:
                for chunk in response.iter_content( chunk_size = 1024 ):
                    if chunk:
                        f.write(chunk)

    else:
        
        path = join(folder,file)

        if not isfile(path):
        
            folder = expanduser('~/.FreeCAD/Mod/yaml-workspace')
        
        path = join(folder,file)

        if not isfile(path):
            print(f'''ERROR: '{ file }' not found!''')
            return

    
    if extension in Part_Extensions:
        insertPart(folder,file,document,group,data)
    else:
        insertMesh(folder,file,document,group,data)
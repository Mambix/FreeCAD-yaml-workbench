
from .Common import defineCommon
from os.path import join
from Mesh import Mesh


def insertMesh ( folder , file , document , group , data : dict | None = None ):

    path = join(folder,file)

    mesh = Mesh(path)

    name = file[:-4]

    if data:
        if 'objectName' in data:
            name = data[ 'objectName' ]
    
    object = document.addObject('Mesh::Feature',name)
    object.Mesh = mesh
    
    if data:
        defineCommon(object,data)

    group.addObject(object)
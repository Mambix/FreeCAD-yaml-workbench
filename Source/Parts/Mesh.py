
from Source.Parts.Common import defineCommon
from os.path import join
from Mesh import Mesh


def insertMesh ( directory , filename , document , group , attributes : dict | None = None ):

    path = join(directory,filename)

    mesh = Mesh(path)

    name = filename[:-4]

    if attributes:
        if 'objectName' in attributes:
            name = attributes[ 'objectName' ]
    
    new_mesh = document.addObject('Mesh::Feature',name)
    new_mesh.Mesh = mesh
    
    if attributes:
        defineCommon(new_mesh,attributes)

    group.addObject(new_mesh)

from Source.Objects.Base import defineBasics
from Mesh import Mesh
from os import path


def insertMesh(directory, filename, document, group, attributes : dict | None = None):
    mesh = Mesh(path.join(directory,filename))
    object_name = filename[:-4]

    if attributes:
        if 'objectName' in attributes:
            object_name = attributes['objectName']
    
    new_mesh = document.addObject("Mesh::Feature", object_name)
    new_mesh.Mesh = mesh
    
    if attributes:
        defineBasics(new_mesh,attributes)

    group.addObject(new_mesh)
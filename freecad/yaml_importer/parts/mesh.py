"""
Provides mesh functions
"""
from os.path import join
from Mesh import Mesh
from .common import define_common


def insert_mesh ( folder , file , document , group , data : dict | None = None ):
    """Function imports mesh object."""
    path = join(folder,file)
    mesh = Mesh(path)
    name = file[:-4]

    if data:
        if 'objectName' in data:
            name = data[ 'objectName' ]

    mesh_object = document.addObject('Mesh::Feature', name)
    mesh_object.Mesh = mesh

    if data:
        define_common(mesh_object, data)
    group.addObject(mesh_object)

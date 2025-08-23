
from Source.Accessors import *
from FreeCAD import Placement
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
        color = getColor(attributes)
        if color:
            new_mesh.ViewObject.ShapeColor = color
        transparency = getTransparency(attributes)
        if transparency:
            new_mesh.ViewObject.Transparency = transparency
        placement = getPlacement(attributes)
        rotation = getRotation(attributes)
        new_mesh.Placement = Placement(placement, rotation)
    group.addObject(new_mesh)
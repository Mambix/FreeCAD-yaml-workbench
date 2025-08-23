
from Source.Accessors import *
from FreeCAD import Placement


def insertCylinder(name, document, group, attributes):
    solid = document.addObject("Part::Cylinder","Cylinder")
    solid.Label = name
    solid.Radius = f'{ attributes[ "radius" ] } mm'
    solid.Height = f'{ attributes[ "height" ] } mm'
    if 'angle' in attributes:
        solid.Angle = f'{ attributes[ "angle" ] } deg'
    color = getColor(attributes)
    if color:
        solid.ViewObject.ShapeColor = color
    transparency = getTransparency(attributes)
    if transparency:
        solid.ViewObject.Transparency = transparency
    placement = getPlacement(attributes)
    rotation = getRotation(attributes)
    solid.Placement = Placement(placement, rotation)
    group.addObject(solid)
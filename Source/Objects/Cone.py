
from Source.Accessors import *
from FreeCAD import Placement


def insertCone(name, document, group, attributes):
    solid = document.addObject("Part::Cone","Cone")
    solid.Label = name
    solid.Radius1 = f'{ attributes[ "radius1" ] } mm'
    solid.Radius2 = f'{ attributes[ "radius2" ] } mm'
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
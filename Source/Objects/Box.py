
from Source.Accessors import *
from FreeCAD import Placement


def insertBox(name, document, group, attributes):
    solid = document.addObject("Part::Box","Box")
    solid.Label = name
    solid.Length = f'{ attributes[ "length" ] } mm'
    solid.Height = f'{ attributes[ "height" ] } mm'
    solid.Width = f'{ attributes[ "width" ] } mm'
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
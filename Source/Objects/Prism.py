
from Source.Accessors import *
from FreeCAD import Placement


def insertPrism(name, document, group, attributes):
    solid = document.addObject("Part::Prism","Prism")
    solid.Label = name
    solid.Polygon = int(attributes[ "polygon" ])
    solid.Circumradius = f'{ attributes[ "radius" ] } mm'
    solid.Height = f'{ attributes[ "height" ] } mm'
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

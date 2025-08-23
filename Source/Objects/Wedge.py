
from Source.Accessors import *
from FreeCAD import Placement


def insertWedge(name, document, group, attributes):
    solid = document.addObject("Part::Wedge","Wedge")
    solid.Label = name
    solid.Xmin = f'{ attributes[ "xmin" ] } mm'
    solid.Ymin = f'{ attributes[ "ymin" ] } mm'
    solid.Zmin = f'{ attributes[ "zmin" ] } mm'
    solid.X2min = f'{ attributes[ "x2min" ] } mm'
    solid.Z2min = f'{ attributes[ "z2min" ] } mm'
    solid.Xmax = f'{ attributes[ "xmax" ] } mm'
    solid.Ymax = f'{ attributes[ "ymax" ] } mm'
    solid.Zmax = f'{ attributes[ "zmax" ] } mm'
    solid.X2max = f'{ attributes[ "x2max" ] } mm'
    solid.Z2max = f'{ attributes[ "z2max" ] } mm'
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

import FreeCAD as App

from Source.Accessors import *


def insertTorus(name, document, group, attributes):
    solid = document.addObject("Part::Torus","Torus")
    solid.Label = name
    solid.Radius1 = f'{ attributes[ "radius1" ] } mm'
    solid.Radius2 = f'{ attributes[ "radius2" ] } mm'
    if 'angle1' in attributes:
        solid.Angle1 = f'{ attributes[ "angle1" ] } deg'
    if 'angle2' in attributes:
        solid.Angle2 = f'{ attributes[ "angle2" ] } deg'
    if 'angle3' in attributes:
        solid.Angle3 = f'{ attributes[ "angle3" ] } deg'
    color = getColor(attributes)
    if color:
        solid.ViewObject.ShapeColor = color
    transparency = getTransparency(attributes)
    if transparency:
        solid.ViewObject.Transparency = transparency
    placement = getPlacement(attributes)
    rotation = getRotation(attributes)
    solid.Placement = App.Placement(placement, rotation)
    group.addObject(solid)
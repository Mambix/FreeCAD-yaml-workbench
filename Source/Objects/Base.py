
from Source.Accessors import *
from FreeCAD import Placement


def defineBasics ( object , attributes ):

    transparency = getTransparency(attributes)
    placement = getPlacement(attributes)
    rotation = getRotation(attributes)
    color = getColor(attributes)


    view = object.ViewObject

    if transparency:
        view.Transparency = transparency

    if color:
        view.ShapeColor = color
    

    object.Placement = Placement(placement,rotation)
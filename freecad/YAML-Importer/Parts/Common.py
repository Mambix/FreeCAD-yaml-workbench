
from ..Getters import *
from FreeCAD import Placement


def defineCommon ( object , data ):

    transparency = getTransparency(data)
    placement = getPlacement(data)
    rotation = getRotation(data)
    color = getColor(data)


    view = object.ViewObject

    if transparency:
        view.Transparency = transparency

    if color:
        view.ShapeColor = color
    

    object.Placement = Placement(placement,rotation)
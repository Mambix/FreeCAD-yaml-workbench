"""
Provides common functions
"""
from ..getters import get_color, get_placement, get_rotation, get_transparency
from FreeCAD import Placement


def define_common ( cad_object , data ):
    """Function defines common settings."""
    transparency = get_transparency(data)
    placement = get_placement(data)
    rotation = get_rotation(data)
    color = get_color(data)
    view = cad_object.ViewObject

    if transparency:
        view.Transparency = transparency

    if color:
        view.ShapeColor = color

    cad_object.Placement = Placement(placement, rotation)

def file_extension(filename):
    """Function returns files extension."""
    extension = filename[-4:]

    if extension[0] == '.':
        extension = extension[1:]
    return extension

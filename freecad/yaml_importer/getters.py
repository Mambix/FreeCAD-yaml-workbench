"""
Provides property extraction functions
"""
from .colors import COLORS
from FreeCAD import Rotation , Vector


Color = tuple[ float , float , float ]


def get_transparency ( data : dict ) -> None | float :
    """Function returns transparency property."""
    return data.get('transparency',None)


def get_placement ( data : dict ):
    """Function returns placement property."""
    config = data.get('placement',None)
    if config:
        return Vector(*config)
    return Vector(0.0,0.0,0.0)


def get_rotation ( data : dict ):
    """Function returns rotation property."""
    points = data.get('rotationVector',(0.0,0.0,1.0))
    angle = data.get('rotationAngle',0.0)
    vector = Vector(*points)
    return Rotation(vector,angle)


def get_color ( data : dict ) -> None | Color :
    """Function returns color property."""
    color = data.get('color', None)

    if not color:
        return None

    if isinstance(color,list):
        return ( color[0] , color[1] , color[2] )

    if color in COLORS:
        return COLORS[ color ]

    raise Exception('Color data needs to be an array of RGB floats or one of predefined colors!')

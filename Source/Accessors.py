

from Source.Colors import Colors
from FreeCAD import Rotation , Vector


Color = tuple[ float , float , float ]


def getTransparency ( data : dict ) -> None | float :
    return data.get('transparency',None)


def getPlacement ( data : dict ) -> object :
    
    config = data.get('placement',None)
    
    if config:
        return Vector(*config)
        
    return Vector(0.0,0.0,0.0)


def getRotation ( data : dict ) -> object :

    points = data.get('rotationVector',(0.0,0.0,1.0))
    angle = data.get('rotationAngle',0.0)

    vector = Vector(*points)

    return Rotation(vector,angle)


def getColor ( data : dict ) -> None | Color :

    color = data.get('color', None)
    
    if not color:
        return None
    
    if isinstance(color,list):
        return ( color[0] , color[1] , color[2] )

    if color in Colors:
        return Colors[ color ]
    
    raise Exception('Color data needs to be an array of RGB floats or one of predefined colors!')
    

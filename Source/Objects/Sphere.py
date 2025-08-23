
from Source.Objects.Base import defineBasics


def insertSphere ( document , attributes ):

    solid = document.addObject('Part::Sphere','Sphere')

    solid.Radius = f'{ attributes[ "radius" ] } mm'

    if 'angle1' in attributes:
        solid.Angle1 = f'{ attributes[ "angle1" ] } deg'

    if 'angle2' in attributes:
        solid.Angle2 = f'{ attributes[ "angle2" ] } deg'

    if 'angle3' in attributes:
        solid.Angle3 = f'{ attributes[ "angle3" ] } deg'
    
    return solid
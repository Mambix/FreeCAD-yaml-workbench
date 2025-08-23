
from Source.Objects.Base import defineBasics


def insertEllipsoid ( name , document , group , attributes ):

    solid = document.addObject('Part::Ellipsoid','Ellipsoid')
    
    solid.Label = name
    
    solid.Radius1 = f'{ attributes[ "radius1" ] } mm'
    solid.Radius2 = f'{ attributes[ "radius2" ] } mm'
    solid.Radius3 = f'{ attributes[ "radius3" ] } mm'
    
    if 'angle1' in attributes:
        solid.Angle1 = f'{ attributes[ "angle1" ] } deg'
 
    if 'angle2' in attributes:
        solid.Angle2 = f'{ attributes[ "angle2" ] } deg'
 
    if 'angle3' in attributes:
        solid.Angle3 = f'{ attributes[ "angle3" ] } deg'
    
    defineBasics(solid,attributes)
    
    group.addObject(solid)
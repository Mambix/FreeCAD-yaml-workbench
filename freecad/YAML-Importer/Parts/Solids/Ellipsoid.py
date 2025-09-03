
def insertEllipsoid ( document , data ):

    solid = document.addObject('Part::Ellipsoid','Ellipsoid')
    
    solid.Radius1 = f'{ data[ "radius1" ] } mm'
    solid.Radius2 = f'{ data[ "radius2" ] } mm'
    solid.Radius3 = f'{ data[ "radius3" ] } mm'
    
    if 'angle1' in data:
        solid.Angle1 = f'{ data[ "angle1" ] } deg'
 
    if 'angle2' in data:
        solid.Angle2 = f'{ data[ "angle2" ] } deg'
 
    if 'angle3' in data:
        solid.Angle3 = f'{ data[ "angle3" ] } deg'
    
    return solid

def insertSphere ( document , data ):

    solid = document.addObject('Part::Sphere','Sphere')

    solid.Radius = f'{ data[ "radius" ] } mm'

    if 'angle1' in data:
        solid.Angle1 = f'{ data[ "angle1" ] } deg'

    if 'angle2' in data:
        solid.Angle2 = f'{ data[ "angle2" ] } deg'

    if 'angle3' in data:
        solid.Angle3 = f'{ data[ "angle3" ] } deg'
    
    return solid
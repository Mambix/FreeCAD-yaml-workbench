
def insertCylinder ( document , attributes ):

    solid = document.addObject('Part::Cylinder','Cylinder')
    
    solid.Radius = f'{ attributes[ "radius" ] } mm'
    solid.Height = f'{ attributes[ "height" ] } mm'
    
    if 'angle' in attributes:
        solid.Angle = f'{ attributes[ "angle" ] } deg'
    
    return solid
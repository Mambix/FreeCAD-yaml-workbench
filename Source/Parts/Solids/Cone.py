
def insertCone ( document , attributes ):

    solid = document.addObject('Part::Cone','Cone')

    solid.Radius1 = f'{ attributes[ "radius1" ] } mm'
    solid.Radius2 = f'{ attributes[ "radius2" ] } mm'
    solid.Height = f'{ attributes[ "height" ] } mm'
  
    if 'angle' in attributes:
        solid.Angle = f'{ attributes[ "angle" ] } deg'
    
    return solid
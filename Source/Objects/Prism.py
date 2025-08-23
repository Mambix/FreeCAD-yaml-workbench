

def insertPrism ( document , attributes ):

    solid = document.addObject('Part::Prism','Prism')
    
    solid.Circumradius = f'{ attributes[ "radius" ] } mm'
    solid.Polygon = int(attributes[ "polygon" ])
    solid.Height = f'{ attributes[ "height" ] } mm'

    return solid

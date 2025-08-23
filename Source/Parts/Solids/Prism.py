
def insertPrism ( document , data ):

    solid = document.addObject('Part::Prism','Prism')
    
    solid.Circumradius = f'{ data[ "radius" ] } mm'
    solid.Polygon = int(data[ "polygon" ])
    solid.Height = f'{ data[ "height" ] } mm'

    return solid

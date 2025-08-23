
def insertBox ( document , attributes ):

    solid = document.addObject('Part::Box','Box')
    
    solid.Length = f'{ attributes[ "length" ] } mm'
    solid.Height = f'{ attributes[ "height" ] } mm'
    solid.Width = f'{ attributes[ "width" ] } mm'
    
    return solid
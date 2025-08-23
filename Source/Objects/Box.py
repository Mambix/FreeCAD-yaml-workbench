
from Source.Objects.Base import defineBasics


def insertBox ( name , document , attributes ):

    solid = document.addObject('Part::Box','Box')

    solid.Label = name
    
    solid.Length = f'{ attributes[ "length" ] } mm'
    solid.Height = f'{ attributes[ "height" ] } mm'
    solid.Width = f'{ attributes[ "width" ] } mm'
    
    defineBasics(solid,attributes)
    
    return solid
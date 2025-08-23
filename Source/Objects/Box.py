
from Source.Objects.Base import defineBasics


def insertBox ( name , document , group , attributes ):

    solid = document.addObject('Part::Box','Box')

    solid.Label = name
    
    solid.Length = f'{ attributes[ "length" ] } mm'
    solid.Height = f'{ attributes[ "height" ] } mm'
    solid.Width = f'{ attributes[ "width" ] } mm'
    
    defineBasics(solid,attributes)
    
    group.addObject(solid)

from Source.Objects.Base import defineBasics


def insertPrism ( name , document , attributes ):

    solid = document.addObject('Part::Prism','Prism')
    
    solid.Label = name

    solid.Circumradius = f'{ attributes[ "radius" ] } mm'
    solid.Polygon = int(attributes[ "polygon" ])
    solid.Height = f'{ attributes[ "height" ] } mm'
    
    defineBasics(solid,attributes)

    return solid

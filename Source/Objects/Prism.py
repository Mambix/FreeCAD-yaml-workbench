
from Source.Objects.Base import defineBasics


def insertPrism(name, document, group, attributes):
    solid = document.addObject("Part::Prism","Prism")
    solid.Label = name
    solid.Polygon = int(attributes[ "polygon" ])
    solid.Circumradius = f'{ attributes[ "radius" ] } mm'
    solid.Height = f'{ attributes[ "height" ] } mm'
    
    defineBasics(solid,attributes)

    group.addObject(solid)

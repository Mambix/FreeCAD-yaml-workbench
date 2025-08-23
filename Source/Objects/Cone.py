
from Source.Objects.Base import defineBasics


def insertCone(name, document, group, attributes):
    solid = document.addObject("Part::Cone","Cone")
    solid.Label = name
    solid.Radius1 = f'{ attributes[ "radius1" ] } mm'
    solid.Radius2 = f'{ attributes[ "radius2" ] } mm'
    solid.Height = f'{ attributes[ "height" ] } mm'
    if 'angle' in attributes:
        solid.Angle = f'{ attributes[ "angle" ] } deg'
    
    defineBasics(solid,attributes)

    group.addObject(solid)
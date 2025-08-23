
from Source.Objects.Base import defineBasics


def insertCylinder ( name , document , group , attributes ):

    solid = document.addObject('Part::Cylinder','Cylinder')
    
    solid.Label = name
    
    solid.Radius = f'{ attributes[ "radius" ] } mm'
    solid.Height = f'{ attributes[ "height" ] } mm'
    
    if 'angle' in attributes:
        solid.Angle = f'{ attributes[ "angle" ] } deg'
    
    defineBasics(solid,attributes)

    group.addObject(solid)
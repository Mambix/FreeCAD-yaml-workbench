
from Source.Objects.Base import defineBasics


def insertWedge ( name , document , group , attributes ):

    solid = document.addObject('Part::Wedge','Wedge')

    solid.Label = name

    keys = [ 
        'Xmin' , 'Ymin' , 'Zmin' ,
        'Xmax' , 'Ymax' , 'Zmax' ,
        'X2min' , 'Z2min' ,
        'X2max' , 'Z2max' 
    ]

    for key in keys:
        setattr(solid,key, f'{ attributes[ key.lower() ] } mm' )

    defineBasics(solid,attributes)

    group.addObject(solid)
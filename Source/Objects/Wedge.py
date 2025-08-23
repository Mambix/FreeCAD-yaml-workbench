
from Source.Objects.Base import defineBasics


def insertWedge ( document , attributes ):

    solid = document.addObject('Part::Wedge','Wedge')

    keys = [ 
        'Xmin' , 'Ymin' , 'Zmin' ,
        'Xmax' , 'Ymax' , 'Zmax' ,
        'X2min' , 'Z2min' ,
        'X2max' , 'Z2max' 
    ]

    for key in keys:
        setattr(solid,key, f'{ attributes[ key.lower() ] } mm' )

    return solid
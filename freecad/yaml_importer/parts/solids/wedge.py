"""
Provides Wedge functions
"""
def insert_wedge ( document , data ):
    """Function inserts FreeCD wedge object."""
    solid = document.addObject('Part::Wedge', 'Wedge')

    keys = [
        'Xmin' , 'Ymin' , 'Zmin' ,
        'Xmax' , 'Ymax' , 'Zmax' ,
        'X2min' , 'Z2min' ,
        'X2max' , 'Z2max' 
    ]

    for key in keys:
        setattr(solid,key, f'{ data[ key.lower() ] } mm' )
    return solid

"""
Provides Cone functions
"""
def insert_cone ( document , data ):
    """Function inserts FreeCD cone object."""
    solid = document.addObject('Part::Cone', 'Cone')
    solid.Radius1 = f'{ data[ 'radius1' ] } mm'
    solid.Radius2 = f'{ data[ 'radius2' ] } mm'
    solid.Height = f'{ data[ 'height' ] } mm'

    if 'angle' in data:
        solid.Angle = f'{ data[ 'angle' ] } deg'

    return solid

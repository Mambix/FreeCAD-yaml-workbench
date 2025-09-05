"""
Provides Cylinder functions
"""
def insert_cylinder ( document , data ):
    """Function inserts FreeCD cylinder object."""
    solid = document.addObject('Part::Cylinder', 'Cylinder')
    solid.Radius = f'{ data[ "radius" ] } mm'
    solid.Height = f'{ data[ "height" ] } mm'

    if 'angle' in data:
        solid.Angle = f'{ data[ "angle" ] } deg'

    return solid

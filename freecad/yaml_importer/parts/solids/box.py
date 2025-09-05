"""
Provides Box functions
"""
def insert_box ( document , data ):
    """Function inserts FreeCD box object."""
    solid = document.addObject('Part::Box', 'Box')
    solid.Length = f'{ data[ 'length' ] } mm'
    solid.Height = f'{ data[ 'height' ] } mm'
    solid.Width = f'{ data[ 'width' ] } mm'

    return solid

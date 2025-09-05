"""
Provides solids functions
"""
from .common import define_common
from .solids import insert_box, insert_cone, insert_cylinder, insert_ellipsoid
from .solids import insert_prism, insert_sphere, insert_torus, insert_wedge


SOLIDS = {
    'box' : insert_box ,
    'cone' : insert_cone ,
    'cylinder' : insert_cylinder ,
    'ellipsoid' : insert_ellipsoid ,
    'prism' : insert_prism ,
    'sphere' : insert_sphere ,
    'torus' : insert_torus ,
    'wedge' : insert_wedge ,
}

def insert_solid ( document , group , name , data ):
    """Function inserts FreeCAD solids."""
    solid_type = data[ 'solid' ]

    if not solid_type in SOLIDS:
        print(f'''ERROR: Unsupported solid type '{ solid_type }' ''')
        return

    solid = SOLIDS[ solid_type ](document, data)
    solid.Label = name
    define_common(solid, data)
    group.addObject(solid)

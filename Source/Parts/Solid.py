
from Source.Parts.Common import defineCommon
from Source.Parts.Solids import *


Solids = {
    'ellipsoid' : insertEllipsoid ,
    'cylinder' : insertCylinder ,
    'sphere' : insertSphere ,
    'wedge' : insertWedge ,
    'torus' : insertTorus ,
    'prism' : insertPrism ,
    'cone' : insertCone ,
    'box' : insertBox
}


def insertSolid ( name , document , group , data ):
    
    type = data[ 'solid' ]

    if not type in Solids:
        print(f'''ERROR: Unsupported solid type '{ type }' ''')
        return
    
    solid = Solids[ type ](document,data)
    solid.Label = name

    defineCommon(solid,data)

    group.addObject(solid)
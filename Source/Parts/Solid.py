
from Source.Parts.Common import defineCommon
from Source.Parts.Solids import *


Shapes = {
    'ellipsoid' : insertEllipsoid ,
    'cylinder' : insertCylinder ,
    'sphere' : insertSphere ,
    'wedge' : insertWedge ,
    'torus' : insertTorus ,
    'prism' : insertPrism ,
    'cone' : insertCone ,
    'box' : insertBox
}


def insertSolid ( name , document , group , attributes ):
    
    type = attributes[ "solid" ]

    if not type in Shapes:
        print(f'ERROR: Unsupported solid type { type }')
        return
    
    shape = Shapes[ type ](document,attributes)
    shape.Label = name

    defineCommon(shape,attributes)

    group.addObject(shape)

from ..Parts import *


def makeElement ( document , group , folder , name , data ):

    if name == 'files':
        
        for file in data:
            insertObject(document,group,folder,file)
        
        return

    if isinstance(data,list):

        for item in data:
            insertObject(document,group,folder,name,item)

    else:

        if 'solid' in data:
            insertSolid(document,group,name,data)
        else:
            insertObject(document,group,folder,name,data)


from .Element import makeElement
from ..Parts import *


def makeGroup ( document , folder , name , data ):

    group = document.addObject('App::DocumentObjectGroup',name)

    if isinstance(data,str):
        insertObject(document,group,folder,data)
        return

    if isinstance(data,list):
        
        for file in data:
            insertObject(document,group,folder,file)

        return

    for name , data in data.items():
        makeElement(document,group,folder,name,data)
   
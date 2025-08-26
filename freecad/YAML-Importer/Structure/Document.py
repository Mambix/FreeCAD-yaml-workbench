
from .Group import makeGroup
from FreeCAD import newDocument


def makeDocument ( folder , name , data ):

    document = newDocument(name)

    for name , data in data.items():
        makeGroup(document,folder,name,data)

    document.recompute()

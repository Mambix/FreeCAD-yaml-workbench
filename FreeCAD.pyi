
GuiUp : bool


class Vector:

    def __init__ (
        self ,
        x : float ,
        y : float ,
        z : float
    ) -> None : ...


class Rotation:

    def __init__ (
        self ,
        vector : Vector ,
        angle : float
    ) -> None : ...


class Placement:

    def __init__ ( 
        self , 
        placement : Vector , 
        rotation : Rotation
    ) -> None : ...



class Document:

    def addObject ( 
        self ,
        * any
    ) -> None : ...

    def recompute ( self ) -> None : ...


def newDocument ( name : str ) -> Document : ...

def addImportType ( * any ) -> None : ...
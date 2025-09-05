"""
Provides group functions
"""
from .element import make_element
from ..parts import insert_object


def make_group ( document , folder , name , data ):
    """Function creates new group."""
    group = document.addObject('App::DocumentObjectGroup',name)

    if isinstance(data,str):
        insert_object(document,group,folder,data)
        return

    if isinstance(data,list):
        for file in data:
            insert_object(document,group,folder,file)

        return

    for name , data in data.items():
        make_element(document,group,folder,name,data)

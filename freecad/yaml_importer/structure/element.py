"""
Provides element functions
"""
from ..parts import insert_object


def make_element ( document , group , folder , name , data ):
    """Function creates new elements."""
    if name == 'files':

        for file in data:
            insert_object(document, group, folder, file)

        return

    if isinstance(data,list):
        for item in data:
            insert_object(document, group, folder, name, item)

    else:

        if 'solid' in data:
            insert_object(document, group, name, data)
        else:
            insert_object(document, group, folder, name, data)

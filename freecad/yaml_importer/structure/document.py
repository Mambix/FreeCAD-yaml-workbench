"""
Provides document functions
"""
from .group import make_group
from FreeCAD import newDocument


def make_document ( folder , document_name , document_data ):
    """Function creates new FreeCAD document."""
    document = newDocument(document_name)

    for name , data in document_data.items():
        make_group(document, folder, name, data)

    document.recompute()

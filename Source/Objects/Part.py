
import FreeCAD as App

from Source.Accessors import *


def insertPart(directory, filename, document, group, attributes = None):
    if not path.isfile(path.join(directory, filename)):
        directory = path.expanduser('~/.FreeCAD/Mod/yaml-workspace')
        if not path.isfile(path.join(directory, filename)):
            print(f'ERROR: `{ filename }` not found!')
            return

    part = Part.Shape()
    part = Part.read(path.join(directory,filename))
    object_name = filename[:-4]
    if 'objectName' in attributes:
        object_name = attributes['objectName']
    new_part = document.addObject("Part::Feature", object_name)
    new_part.Shape = part
    if attributes:
        color = getColor(attributes)
        if color:
            new_part.ViewObject.ShapeColor = color
        transparency = getTransparency(attributes)
        if transparency:
            new_part.ViewObject.Transparency = transparency
        placement = getPlacement(attributes)
        rotation = getRotation(attributes)
        new_part.Placement = App.Placement(placement, rotation)
    group.addObject(new_part)
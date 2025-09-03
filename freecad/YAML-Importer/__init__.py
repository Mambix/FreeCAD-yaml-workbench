
from FreeCAD import addImportType


print('YAML-Workbench::__init__')


addImportType(
    'YAML script (*.yml)' , 
    'freecad.YAML-Importer.Open'
)


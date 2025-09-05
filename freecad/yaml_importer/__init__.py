"""
Provides yaml workbench
"""
import FreeCAD


print('YAML-Workbench::__init__')


FreeCAD.addImportType('YAML script (*.yml)' , 'freecad.yaml_importer.open' )

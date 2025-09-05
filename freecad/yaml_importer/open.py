"""
Provides yaml settings functions
"""
from os.path import expanduser , exists , dirname , join
from os import makedirs
from builtins import open as pyopen
from yaml import safe_load
from .structure.document import make_document
from FreeCAD import GuiUp


print('YAML-Workbench::init_gui')


if GuiUp:
    import FreeCADGui as Gui # type: ignore


def open ( yaml_file ):
    """Function called when you open file in FreeCAD."""
    yaml_file_folder = dirname(yaml_file)

    cache_folder = expanduser('~/.FreeCAD/Mod/yaml-workbench')

    print(f'''Reading: '{ yaml_file }' ''')
    print(f'''Base: '{ yaml_file_folder }' ''')
    print(f'''Cache: '{ cache_folder }' ''')

    yaml_data = None

    with pyopen(yaml_file) as file:
        yaml_data = safe_load(file)

    if yaml_data is None:
        raise Exception(f'''Error reading YAML file: '{ yaml_file }' ''')

    print(f'YAML data: { yaml_data }')

    if 'settings' in yaml_data:
        if 'subDirectory' in yaml_data[ 'settings' ]:

            sub_directory = yaml_data[ 'settings' ][ 'subDirectory' ]

            if sub_directory[0:4] == 'http':

                yaml_file_folder = sub_directory

                if not exists(cache_folder):
                    makedirs(cache_folder)
            else:
                yaml_file_folder = join(yaml_file_folder, sub_directory)

            print(f'''Base: '{ yaml_file_folder }' ''')

    if 'import' not in yaml_data:
        raise Exception('''No 'import' section in YAML file!''')

    imports = yaml_data[ 'import' ]

    for name , yaml_data in imports.items():
        make_document(yaml_file_folder, name, yaml_data)

    Gui.activeDocument().activeView().viewAxonometric() # type: ignore
    Gui.SendMsgToActiveView('ViewFit') # type: ignore

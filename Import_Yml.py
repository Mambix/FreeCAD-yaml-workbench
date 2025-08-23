
from Source.Structure.Document import makeDocument
from builtins import open as openFile
from os.path import dirname , join
from FreeCAD import GuiUp
from yaml import safe_load


if GuiUp:
    import FreeCADGui as Gui # type: ignore


def open ( path ):

    folder = dirname(path)
    
    print(f'''Reading: '{ path }' ''')
    print(f'''Base: '{ folder }' ''')

    data = None

    with openFile(path) as file:
        data = safe_load(file)

    if data is None:
        raise Exception(f'''Error reading YAML file: '{ path }' ''')

    print(f'YAML data: { data }')

    if 'settings' in data:
        if 'subDirectory' in data[ 'settings' ]:
            
            subfolder = data[ 'settings' ][ 'subDirectory' ]

            folder = join(folder,subfolder)

            print(f'''Base: '{ folder }' ''')

    if 'import' not in data:
        raise Exception('''No 'import' section in YAML file!''')

    imports = data[ 'import' ]

    for name , data in imports.items():
        makeDocument(folder,name,data)

    Gui.activeDocument().activeView().viewAxonometric() # type: ignore
    Gui.SendMsgToActiveView('ViewFit') # type: ignore

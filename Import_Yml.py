
from Source.Parts import *
from builtins import open as openFile
from FreeCAD import newDocument , GuiUp
from os.path import dirname , join
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

    data = data[ 'import' ]

    for document_name , document_data in data.items():

        document = newDocument(document_name)

        for group_name , group_data in document_data.items():

            group = document.addObject('App::DocumentObjectGroup',group_name)

            if isinstance(group_data,str):
                insertObject(folder,group_data,document,group)
                continue

            if isinstance(group_data,list):
                
                for file in group_data:
                    insertObject(folder,file,document,group)

                continue

            for file , file_data in group_data.items():

                if file == 'files':
                
                    for file in file_data:
                        insertObject(folder,file,document,group)
                    continue

                if not isinstance(file_data,list):

                    if 'solid' in file_data:
                        insertSolid(file,document,group,file_data)
                    else:
                        insertObject(folder,file,document,group,file_data)
                else:

                    for file_data2 in file_data:
                        insertObject(folder,file,document,group,file_data2)
                        
        document.recompute()

    Gui.activeDocument().activeView().viewAxonometric() # type: ignore
    Gui.SendMsgToActiveView("ViewFit") # type: ignore

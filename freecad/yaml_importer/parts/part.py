"""
Provides parts functions
"""
from os.path import expanduser , isfile , join
from Part import Shape , read
from requests import get as fetch
from .common import define_common, file_extension
from ..crypto import calculate_sha256


def insert_part ( folder_or_url , filename , document , group , data : dict | None = None ):
    """Function inserts FreeCAD parts."""
    extension = file_extension(filename)

    if folder_or_url[0:4] == 'http':
        url = f'{ folder_or_url }/{ filename }'
        hashed_file_name = f'{ calculate_sha256(url) }.{ extension }'
        folder_or_url = expanduser('~/.FreeCAD/Mod/yaml-workbench')
        full_file_name = join(folder_or_url, hashed_file_name)

        if not isfile(full_file_name):
            print(f'Fetching object from \'{ url }\'')
            response = fetch(url, stream = True, timeout=60 )
            if not response.ok:
                print(f'ERROR: `{ url }` not found!')
                return

            with open(full_file_name,'wb+') as f:
                for chunk in response.iter_content( chunk_size = 1024 ):
                    if chunk:
                        f.write(chunk)
    else:
        full_filename = join(folder_or_url, filename)
        if not isfile(full_filename):
            folder_or_url = expanduser('~/.FreeCAD/Mod/yaml-workbench')
        full_filename = join(folder_or_url, filename)

        if not isfile(full_filename):
            print(f'''ERROR: '{ filename }' not found!''')
            return

    shape = Shape()
    shape = read(full_filename)
    name = filename[:-4]
    if data:
        if 'objectName' in data:
            name = data[ 'objectName' ]

    document_object = document.addObject('Part::Feature', name)
    document_object.Shape = shape

    if data:
        define_common(document_object, data)

    group.addObject(document_object)

"""
Provides object functions
"""
from os.path import expanduser , isfile , join
from requests import get as fetch
from .common import file_extension
from ..crypto import calculate_sha256
from .mesh import insert_mesh
from .part import insert_part


PART_EXTENSIONS = [ '.stp', '.igs', 'iges', 'step' ]


def insert_object ( document , group , folder_or_url , filename , data : dict | None = None ):
    """Function creates new FreeCAD objects."""
    extension = file_extension(filename)
    full_file_name = filename

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
        full_file_name = join(folder_or_url, filename)
        if not isfile(full_file_name):
            folder_or_url = expanduser('~/.FreeCAD/Mod/yaml-workbench')
        full_file_name = join(folder_or_url, filename)

        if not isfile(full_file_name):
            print(f'''ERROR: '{ full_file_name }' not found!''')
            return

    if extension in PART_EXTENSIONS:
        insert_part(folder_or_url, full_file_name, document, group, data)
    else:
        insert_mesh(folder_or_url, full_file_name, document, group, data)

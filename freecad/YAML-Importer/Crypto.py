
from hashlib import sha256


def hash ( value : str ):

    encoded = value.encode('utf-8')
    
    hash = sha256(encoded)
    
    digest = hash.hexdigest()

    return digest
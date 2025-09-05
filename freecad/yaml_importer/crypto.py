"""
Provides hashing functions
"""
from hashlib import sha256


def calculate_sha256 ( value : str ):
    """Function returns SHA256 hash for a given string."""
    encoded = value.encode('utf-8')
    calculated_hash = sha256(encoded)
    digest = calculated_hash.hexdigest()
    return digest

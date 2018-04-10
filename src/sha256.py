from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

def hash(data, nonce):
    """Generates a hashcode of the given input using the SHA256 algorithm
    Arguments:
    data -- The binary data to be hashed
    nonce -- The value appended to the provided data before hashing

    Returns:
    The bytes of the resulting hashcode
    """
    if(not isinstance(data, bytes)):
        raise TypeError("data must be of type 'bytes'")

    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(data + str(nonce).encode())
    return digest.finalize()
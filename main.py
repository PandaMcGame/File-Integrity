import hashlib


def hash_file(file_path: str):
    """"This function returns the SHA-256 hash
   of the file passed into it."""

    # make a hash object
    h = hashlib.sha256()

    # open file for reading in binary mode
    with open(file_path, 'rb') as file:
        # loop till the end of the file
        chunk = 0
        while chunk != b'':
            # read only 1024 bytes at a time
            chunk = file.read(1024)
            h.update(chunk)

    # return the hex representation of digest
    return h.hexdigest()


def file_integrity_verifier(original: str, file: str) -> bool:
    if hash_file(original) != hash_file(file):
        return False
    return True


print(file_integrity_verifier("demo/test.txt", "demo/test2.txt"))
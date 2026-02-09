import hashlib

def sha256_hasher(input_string):
    print("Input string to hash: " + input_string)
    data_bytes = input_string.encode("utf-8")
    hash_obj = hashlib.sha256(data_bytes)
    hexadec_rep = hash_obj.hexdigest()
    print("SHA-256 hash (hexadecimal representation): " + hexadec_rep)

input_string = input("Enter the string to hash: ")
sha256_hasher(input_string)

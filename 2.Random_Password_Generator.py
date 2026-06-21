import string
import random

def rand_pass_gen(length = 8):

    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for i in range(length))
    return password

pass_len_str = input("Enter the length of password (default: 8 characters): ")

if pass_len_str:
    length = int(pass_len_str)
else:
    length = 8

password = rand_pass_gen(length)
print("Generated password: " + password)
from .keys import readfile, get_rsa_cipher
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES
import base64
import ntpath
import os

def encrypt(filepath, publicKeyPath):
    head, filename = ntpath.split(filepath)
    filename_size = len(filename)
    filename_bytes = int.to_bytes(filename_size, 2, 'big')
    contents_in_binary = readfile(filepath) # read in binary

    new_random_filename = ''.join('ct') # name of file

    # Creating AES key
    session_key = get_random_bytes(16)
    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    # Encrypting the compressed text
    cipherdata, tag = cipher_aes.encrypt_and_digest(contents_in_binary)

    cipher_rsa, _ = get_rsa_cipher(publicKeyPath) # Getting the public key
    encrypted_session_key = cipher_rsa.encrypt(session_key) # Encrypting AES Key with the RSA Public Key
    
    # This is our final encrypted data
    finalenc = encrypted_session_key + cipher_aes.nonce + tag
    finalenc += filename_bytes 
    finalenc += bytes(filename, 'utf-8') # filename in bytes
    finalenc += cipherdata

    # base64 encode and write to file
    encrypted = base64.encodebytes(finalenc)
    output_path = os.path.join(head, new_random_filename)
    with open(f"{output_path}.encrypted", 'wb') as output:
        output.write(encrypted)
    return(encrypted)

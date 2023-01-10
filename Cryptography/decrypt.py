from Cryptodome.Cipher import AES
from .keys import get_rsa_cipher, readfile
from io import BytesIO
import base64
import os
import ntpath

"""
    this function is for decrypting files,
    -encrypted_bytes- variable is consist of 6 main sections:
        --1th section is encrypted AES key,
        --2th section is AES nonce,
        --3th section is tag,
        --4th section is filename size in bytes,
        --5th section is filename in bytes format, we decode it to 'utf-8'
        --6th section is our encrypted data(encrypted with AES)
    then we will base64 encode the whole payload and write it down to a file
"""

def decrypt(filepath, privateKeyPath):

    # read data in binary
    data = readfile(filepath)

    # Decrypt with private key
    encrypted_bytes = BytesIO(base64.decodebytes(data))
    cipher_rsa, keysize_in_bytes = get_rsa_cipher(privateKeyPath)
    encrypted_session_key = encrypted_bytes.read(keysize_in_bytes)
    nonce = encrypted_bytes.read(16)
    tag = encrypted_bytes.read(16)
    filename_size_in_bytes = encrypted_bytes.read(2)
    filename_size = int.from_bytes(filename_size_in_bytes, 'big')
    filename = (encrypted_bytes.read(filename_size)).decode("utf-8") 
    cipherData = encrypted_bytes.read()
    session_key = cipher_rsa.decrypt(encrypted_session_key)
    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
    decrypted = cipher_aes.decrypt_and_verify(cipherData, tag)

    # Returns decrypted file, which is the original file
    head, _ = ntpath.split(filepath)
    original_file_path = os.path.join(head, filename)
    with open(original_file_path, 'wb') as output:
        output.write(decrypted)
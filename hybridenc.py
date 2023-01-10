from Cryptography.arguments import get_arguments
import argparse

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-g', '--generate', help='Sets path to generate and save RSA private and public keys.')
    parser.add_argument('-e', '--encrypt', action='store_true', help='Encrypts the given file into ct_encrypted.')
    parser.add_argument('-d', '--decrypt', action='store_true', help='Decrypts ct_encrypted file.')
    parser.add_argument('-f', '--files', nargs='+',help='Passes directory/file to encrypt/decrypt.')
    parser.add_argument('-x', '--extension', nargs='+', help='Looks for specific files.')
    parser.add_argument('-priv', '--PrivateKey', help='Passes directory to key.priv.')
    parser.add_argument('-pub', '--PublicKey', help='Passes directory to key.pub.')
    parser.add_argument('-delete', '--DELETE', action='store_true', help='Removes original file after encrypting.')
    args = parser.parse_args()

    # calls function to handle arguments
    get_arguments(args)

if __name__ == '__main__':
    main()
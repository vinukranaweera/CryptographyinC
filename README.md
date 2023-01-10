# 480 Final Project – CCA2 Hybrid Encryption
Project by Vinuk Ranaweera
Created in Visual Studio Code on macOS

## Required Installations
Run the following command in the terminal:
```bash 
make
```
Then, open a new terminal and program will be ready for use.

## How To Use
```bash
# Step 1: Generate RSA Public and RSA Private Keys
python hybridenc.py -g (filepath to store keys)
# Step 2: # Encrypt file and writes encrytion in ct.encrypted  (optional: use -delete to delete original file with after encryption)
python hybridenc.py -e -f ["file" "filepath"] -x ["file_extension"] -pub /(filepath)/key.pub -delete 
# Step 3: Decrypt ct.encrypted file (automatically deletes encrypted file)
python hybridenc.py -d -f ct.encrypted ["filepath"] -priv /(filepath)/key.priv 
```

## Examples of Use
Example: a folder named 'crypto' and a txt named 'hellocrypto' was created in macOS: 
```bash
python hybridenc.py -g /Users/crypto/

python hybridenc.py -e -f hellocrypto.txt /Users/crypto -x .txt -pub /Users/crypto/key.pub -delete 

python hybridenc.py -d -f ct.encrypted /Users/crypto -priv /Users/crypto/key.priv 
```

## Notes
HMAC was not implemented.
If make is not working, first create virtual environment with the following command:
```bash 
python3 -m venv .venv
source .venv/bin/activate
```
After executing this, then open a new termnial and run the required installations.

To clean the cache, run command in terminal:
```bash 
make clean
```

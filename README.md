# RSA

## Video presentation

[![YouTube video](http://img.youtube.com/vi/mJqqK9U2bRc/0.jpg)](http://www.youtube.com/watch?feature=player_embedded&v=mJqqK9U2bRc)

## Goal

The aim of the project is to implement the RSA cryptographic algorithm. Additionally, the implementation of the process of loading and using text data, as well as the process of saving this data to a file, or displaying this data. The program also has the implementation of the function of saving data to a file, or their execution.

## Used tools

- Programming language [Python](https://www.python.org/doc/) (version 3.11.0)
  - Module [rsa](https://github.com/sybrenstuvel/python-rsa)
  - Module [argparse](https://docs.python.org/3/library/argparse.html)
- [Visual Studio Code](https://code.visualstudio.com/)

## Basic structure

```cmd
./main.py
./keys
./execute_commands.py
```

_For the program to run properly, the keys folder is needed in the same location as main.py_

## Usage

### Display help

```cmd
python main.py -h
```

```cmd
λ python main.py -h
usage: main.py [-h] [-text TEXT] [-loadText LOADTEXT] [-encryptedFile ENCRYPTEDFILE]
               [-save SAVE] [-encryption] [-decryption] [-genKeys] [-showEncryptedText]

RSA encryption consists in generating a pair of keys (private key, public key). The
message is then encrypted with the public key. Finally, the process of decrypting the
message using the private key is carried out.

options:
-h, --help            show this help message and exit
-text TEXT            Enter text
-loadText LOADTEXT    Read text from a file
-encryptedFile ENCRYPTEDFILE
                      A file with encrypted data
-save SAVE            Use to save the decrypted text to a file
-encryption           Use for encryption
-decryption           Use to decrypt
-genKeys              Use to generate a new key pair
-showEncryptedText    Use to display ciphertext

__________
```

### Example usage

```cmd
python main.py -encryption -genKeys -text "przykładowy tekst"
python main.py -decryption

python main.py -encryption -text "Ciekawostki nr 1"
python main.py -decryption

python main.py -encryption -text "Ciekawostki nr 2" -encryptedFile a.txt
python main.py -decryption -encryptedFile a.txt

python main.py -encryption -genKeys -loadText tekst.txt
python main.py -decryption

python main.py -encryption -loadText tekst.txt
python main.py -decryption
```

## Automated test of functionality

```cmd
python execute_commands.py
```

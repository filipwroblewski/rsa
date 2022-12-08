import rsa
import argparse


def genKeys(length: int = 512):
    """
    Generating a key pair.

    :param length: The number of key lengths in bits (minimum 16 bits)
    :type n: int
    :raise TypeError: If length does not have type int
    :return: Returns a public, private key pair
    :rtype: tuple
    """
    return rsa.newkeys(length)


def encrypt(text: str, publicKey: rsa.key.PublicKey):
    """
    Encryption.

    :param text: The text to be encrypted
    :type text: str
    :param publicKey: The public key used for encryption
    :type publicKey: rsa.key.PublicKey
    :raise TypeError: If publicKey does not have type rsa.key.PublicKey
    :return: Returns the encrypted text with the public key, which is encoded as a byte
    :rtype: byte
    """
    return rsa.encrypt(text.encode(),
                       publicKey)


def decrypt(encryptedText: bytes, privateKey: rsa.key.PrivateKey):
    """
    Decryption.

    :param encryptedText: Encrypted message
    :type encryptedText: bytes
    :param privateKey: The private key used for decryption
    :type privateKey: rsa.key.privateKey
    :raise TypeError: If encryptedText has no bytes type
    :raise TypeError: If privateKey does not have type rsa.key.privateKey
    :return: Returns the decrypted message with the private key
    :rtype: str
    """
    return rsa.decrypt(encryptedText, privateKey).decode()


def save_to_file(f_name, to_save, f_type='wb'):
    """
    Writing to a file.

    :param f_name: File name
    :type f_name: str
    :param to_save: The text to be saved
    :type to_save: str
    :param f_type: The type of file handling
    :type f_type: str
    :raise FileNotFoundError: If the specified file cannot be found in f_name
    """
    with open(f_name, f_type) as f:
        f.write(to_save)


def load_from_file(f_name, f_type='rb'):
    """
    Loading data from a file.

    :param f_name: File name
    :type f_name: str
    :param f_type: The type of file handling
    :type f_type: str
    :raise FileNotFoundError: If the specified file cannot be found in f_name
    :return: Returns text from a file
    :rtype: Depends on f_type
    """
    with open(f_name, mode=f_type) as f:
        return f.read().rstrip()


parser = argparse.ArgumentParser(
    description='''
    RSA encryption consists in generating a pair of keys (private key, public key).
    The message is then encrypted with the public key.
    Finally, the process of decrypting the message using the private key is carried out.
    ''', epilog='__________')

parser.add_argument("-text", default="", help="Enter text", type=str)
parser.add_argument("-loadText", default="",
                    help="Read text from a file", type=str)
parser.add_argument("-encryptedFile", default="",
                    help="A file with encrypted data", type=str)
parser.add_argument("-save", default="",
                    help="Use to save the decrypted text to a file", type=str)

parser.add_argument("-encryption", action="store_true",
                    help="Use for encryption")
parser.add_argument("-decryption", action="store_true",
                    help="Use to decrypt")
parser.add_argument("-genKeys", action="store_true",
                    help="Use to generate a new key pair")
parser.add_argument("-showEncryptedText", action="store_true",
                    help="Use to display ciphertext")

args = parser.parse_args()

(encryptedFile := 'zaszyfrowanyTekst.txt') if args.encryptedFile == '' else (
    encryptedFile := args.encryptedFile)

if args.encryption:
    print('Encryption...')
    if args.genKeys:
        print('Key generation...')
        publicKey, privateKey = genKeys()
        try:
            publicKeyPath = 'keys/publicKey.pem'
            print(f'Write the public key to {publicKeyPath}...')
            save_to_file(f_name=publicKeyPath,
                         to_save=publicKey.save_pkcs1('PEM'))

            privateKeyPath = 'keys/privateKey.pem'
            print(f'Saving the private key to {privateKeyPath}...')
            save_to_file(f_name=privateKeyPath,
                         to_save=privateKey.save_pkcs1('PEM'))
        except:
            print(
                'Problem with saving keys to files. Check if the keys folder exists')
            exit()
    else:
        try:
            publicKey = rsa.PublicKey.load_pkcs1(
                load_from_file(f_name='keys/publicKey.pem'))
        except:
            print(
                'Problem with loading keys from file. Check if you have keys folder')
            exit()

    if args.loadText == '':
        encMessage = encrypt(args.text, publicKey)
    else:
        try:
            text_from_file = load_from_file(f_name=args.loadText, f_type='r')
            print(f'Loaded from data: {str(text_from_file)}')

        except:
            print(
                f'Error loading file from given path. Given path "{args.loadText}"')
            exit()
        finally:
            encMessage = encrypt(text_from_file, publicKey)

    if args.showEncryptedText:
        print(
            f'Encrypted message: {str(encMessage)[2:-1]}')
    try:
        save_to_file(f_name=encryptedFile, to_save=encMessage)
        print(f'The encrypted text was saved in {encryptedFile}')
    except:
        print('Problem with saving the encrypted file')
        exit()


elif args.decryption:
    print('Decryption...')
    try:
        privateKey = rsa.PrivateKey.load_pkcs1(
            load_from_file(f_name='keys/privateKey.pem'))
        encMessage = load_from_file(f_name=encryptedFile)
        decMessage = decrypt(encMessage, privateKey)

        if args.save != '':
            try:
                print('Saving the decrypted text to a file...')
                decryptedFile = args.save
                with open(decryptedFile, 'w', encoding="utf-8") as f:
                    f.write(decMessage)
                print(
                    f'The decrypted text was saved in {decryptedFile}')
            except:
                print('Problem with saving decrypted file')
                exit()
        else:
            print("Decrypted text: ", decMessage)

    except:
        print(
            'Problem with loading keys from file. Check if you have keys folder')
        exit()

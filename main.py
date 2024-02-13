import os
from cryptography.fernet import Fernet

def get_key():
    #Check if key does not exist
    if not os.path.exists("secret_key.bin"):
        #Generate new Fernet key
        key = Fernet.generate_key()
        #Write key to file 'secret_key.bin' in the same directory as the script
        with open("secret_key.bin", "wb") as f:
            f.write(key)

    #Read the key
    with open("secret_key.bin", "rb") as f:
        key = f.read()

    return key   

#Get mode of cryptography from user
def get_mode():
    while True:
        mode = input("(E)ncrypt/(D)ecrypt?: ").lower()
        
        if mode == "e" or mode == "d":
            return mode
        else:
            print("Invalid option")

#Get the file and filepath to encrypt/decrypt
def get_file():
    file_path = input("Enter absolute path of file without quotations: ")

    #Remove quotes if the user did input path that includes quotes
    file_path = file_path.replace('"', '')

    with open(file_path, "rb") as f:
        file_contents = f.read()
    
    return file_path, file_contents

#Perform the encryption/decryption of the file
def perform_crypt(key, mode, file_contents, file_path):
    f = Fernet(key)

    match mode:
        case "e":
            data = f.encrypt(file_contents)
        case "d":
            data = f.decrypt(file_contents)
    
    #Write the file to the same path and name
    with open(file_path, "wb") as f:
        f.write(data)

if __name__ == "__main__":
    
    #Get Fernet key
    key = get_key()
    
    #Get mode
    mode = get_mode()

    #Get file path and contents of file
    file_path, file_contents = get_file()

    perform_crypt(key, mode, file_contents, file_path)

    print("Done")
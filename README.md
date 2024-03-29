
# PyCr - Cryptography using Fernet

PyCr is powerful tool used to encrypt and decrypt files from the command line. PyCr utilises a strong cryptographic algorithm 'Fernet' from the Cryptography library. 

Fernet guarantees that a message encrypted using it cannot be manipulated or read without the key, ensuring your files remain secure and can only be decrypted by you.

PyCr on first boot generates a Fernet key, this will be stored in the same directory as where you ran the script from. The key must be in the same directory for PyCr to perform encryption/decryption on your files.

PyCr's simple command-line functionality provides an easy and reliable solution for encrypting your personal files to ensure no one but you can read them.

# Usage

Write 'python main.py' in your terminal and follow the dialogue to use the program.

# Disclaimer

The original file will be **OVERWRITTEN** with the encrypted version.

Any files encrypted with 'secret_key.bin' will be **IRRECOVERABLE** if the 'secret_key.bin' file is lost or deleted! Make sure to have multiple backups.

This tool is for educational purposes only. Depending on your requirements, other public encryption tools might be better to secure your files.

# Limitations

Fernet is ideal for encrypting data that easily fits in memory. As a design feature it does not expose unauthenticated bytes. This means that the complete message contents must be available in memory, making Fernet generally unsuitable for very large files at this time. Taken from (https://cryptography.io/en/latest/fernet/)

# Dependencies

- Python 3+
- pyca/cryptography library (pip install cryptography)

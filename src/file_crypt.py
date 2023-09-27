from cryptography.fernet import Fernet


def encrypt_and_get_key(file_path: str):

    key = Fernet.generate_key()
    cipher = Fernet(key)

    with open(file_path, "rb") as file:
        file_data = file.read()

    encrypted_data = cipher.encrypt(file_data)
    with open(file_path, "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

    return key


def decrypt(file_path, key):
    cipher = Fernet(key)
    with open(file_path, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()

    decrypted_data = cipher.decrypt(encrypted_data)
    with open(file_path, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

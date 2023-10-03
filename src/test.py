from cryptography.fernet import Fernet

# Generate a new Fernet key
key = Fernet.generate_key()
print("Generated Fernet key:", key)


# Basic python script to showcase encryption using fernet. This code is strictly for educational/testing purposes 
#!/usr/bin/env python3
import os
import sys
from cryptography.fernet import Fernet

key = Fernet.generate_key()
fernet = Fernet(key)

print(key)

path = input("Please input a directory to encrypt: ")

if not os.path.exists(path):
    print(f"Path not found: {path}")
    sys.exit(1)



print(f"\nStarting encryption in directory: {path}\n")

for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".encrypted"):
            print(f"Skipping already encrypted file: {file}")
            continue
        full_path = os.path.join(root, file)
        try:
            with open(full_path, "rb") as f:
                orig = f.read()
            enc = fernet.encrypt(orig)
            enc_path = full_path + ".encrypted"
            with open(enc_path, "wb") as s:
                s.write(enc)
            try:
                os.remove(full_path)
                print(f"Deleted file {full_path}")
            except Exception as f:
                print(f"Failed to delete file: {f}")
            print(f"File '{full_path}' encrypted to '{enc_path}'")
        except Exception as e:
            print(f"Failure to encrypt {full_path}: {e}")

print("Encryption Complete!")

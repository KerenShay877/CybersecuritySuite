# secure_file_deletion.py

import os

def secure_delete(file_path):
    try:
        with open(file_path, "wb") as file:
            file.write(os.urandom(os.path.getsize(file_path)))
        os.remove(file_path)
        print(f"File securely deleted: {file_path}")
    except Exception as e:
        print(f"Error deleting file: {e}")

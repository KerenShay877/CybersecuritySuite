import itertools
import string
import hashlib

def crack_password(hash_to_crack, max_length=4):
    characters = string.ascii_letters + string.digits + string.punctuation
    attempts = 0

    for length in range(1, max_length + 1):
        for candidate in itertools.product(characters, repeat=length):
            password_attempt = ''.join(candidate)
            hashed_attempt = hashlib.sha256(password_attempt.encode()).hexdigest()

            attempts += 1

            if hashed_attempt == hash_to_crack:
                print(f"Password cracked: {password_attempt}")
                print(f"Total attempts: {attempts}")
                return

    print("Password not found within the specified length limit.")

# Example usage
hashed_password = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"  # SHA-256 hash of "password"
crack_password(hashed_password, max_length=4)

# main.py

from port_scanner import port_scanner
from password_cracker import password_cracker
from encryption import caesar_cipher, substitution_cipher, vigenere_cipher, hashing_algorithms
from secure_file_deletion import secure_file_deletion
from web_security_scanner import web_security_scanner
from ssl_certificate_scanner import ssl_certificate_scanner

def print_menu():
    print("\n Cybersecurity Suite Menu:")
    print("1. Port Scanner")
    print("2. Password Cracker")
    print("3. Caesar Cipher")
    print("4. Substitution Cipher")
    print("5. Vigenere Cipher")
    print("6. Hashing Algorithms")
    print("7. Secure File Deletion")
    print("8. Web Security Scanner")
    print("9. SSL Certificate Scanner")
    print("0. Exit")

def main():
    while True:
        print_menu()
        choice = input("Enter the number of the module to run (0 to exit): ")

        if choice == '0':
            print("Exiting Cybersecurity Suite. Goodbye!")
            break
        elif choice == '1':
            port_scanner.run_port_scanner()
        elif choice == '2':
            password_cracker.run_password_cracker()
        elif choice == '3':
            caesar_cipher.run_caesar_cipher()
        elif choice == '4':
            substitution_cipher.run_substitution_cipher()
        elif choice == '5':
            vigenere_cipher.run_vigenere_cipher()
        elif choice == '6':
            hashing_algorithms.run_hashing_algorithms()
        elif choice == '7':
            secure_file_deletion.run_secure_file_deletion()
        elif choice == '8':
            web_security_scanner.run_web_security_scanner()
        elif choice == '9':
            ssl_certificate_scanner.run_ssl_certificate_scanner()
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()

import hashlib
import sys

def main():
    original_hash = input("Inform the original hash: ")
    hash_algorithm = int(input("Inform the hash algorithm (md5 = 1, sha256 = 2: "))

    with open(sys.argv[1], 'rb') as f:
        file = f.read()

    if hash_algorithm == 1:
        hashed_file = hashlib.md5(file).hexdigest()
    elif hash_algorithm == 2:
        hashed_file = hashlib.sha256(file).hexdigest()
    else:
        print("Valor inválido.")
        exit()

    if original_hash != hashed_file:
        print("Wrong!")
    else:
        print("Good.")

if __name__ == "__main__":
    main()
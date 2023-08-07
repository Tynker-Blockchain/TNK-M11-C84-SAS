# Import hashlib library
import hashlib

def generateHash(inputString):

    # Create a hash object using SHA-256 algorithm
    hashObject = hashlib.sha256()
    # Convert the input string to bytes and update the hash object
    hashObject.update(inputString.encode('utf-8'))
    # Get the hexadecimal representation of the hash
    hash_value = hashObject.hexdigest()

    return hash_value


inputString = "Hello, Convert me into a hash."
print("Input String:", inputString)
hashValue = generateHash(inputString)
print("Hash value:", hashValue)

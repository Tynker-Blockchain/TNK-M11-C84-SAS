def generateHash(inputString):
    hashValue = 0
    # Create a variable prime and hashLength and assign them a prime number and length of hash you want to generate
    prime = 31
    hashLength = 8

    for char in inputString:
        # Calculate hash as:
        hashValue = (hashValue * prime + ord(char))
        #hashValue += ord(char)

    # Truncating the Hash to a Fixed Length
    hashValue = hashValue % 10 **  hashLength
    
    # Convert the hash value to a fixed-length string by padding with zeros if necessary
    hashValue = str(hashValue).zfill(hashLength)    

    return hashValue

# Try different input string and see if length of output hash is equal
inputString = "Hello, Conver me into a hash."
print("Input String:", inputString)
hashValue = generateHash(inputString)
print("Hash value:", hashValue)


inputString = "Hi, I am another string of different length."
print("Input String:", inputString)
hashValue = generateHash(inputString)
print("Hash value:", hashValue)




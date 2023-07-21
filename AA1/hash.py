# find out the erros in the code and fix them
def generateHash(inputString):
    hashValue = 0
    
    # Use for loop instead of if statement
    if char in inputString:
        # Add ASCII value to the hashValue
        hashValue = ord(char)
           
    return hashValue

inputString = "Hello, Conver me into a hash."

print("Input String:", inputString)
hashValue = generateHash(inputString)
print("Hash value:", hashValue)


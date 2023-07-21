# Define function named generatehash with parameter inputString
def generateHash(inputString):
    # Initialize the hash value to 0
    hashValue = 0
    # Iterate over each character in the input string
    for char in inputString:
        # Update the hash value by adding the ASCII value of the character
        hashValue += ord(char)
    # Return the hash value    
    return hashValue

inputString = "Hello, Conver me into a hash."

print("Input String:", inputString)
# Call generate Hash() function with 'inputString' and store the results in 'hashValue' variable
hashValue = generateHash(inputString)

# Print the hash value 
print("Hash value:", hashValue)


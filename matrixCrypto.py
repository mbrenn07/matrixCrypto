initialString = "automate nearly everything"
keyMatrix = [3,1,4,9]
createdMatrix = []
encryptedMatrix = []
encryptedString = ""
alphabet = " abcdefghijklmnopqrstuvwxyz"
alphabetDict = {}
reversedAlphabetDict = {}

if len(initialString) == 0:
    initialString = input("give me the big string to encrypt")
if (len(initialString)%2!=0):
    print("\033[91mthat's odd, no way im trying to encode it")
    exit()
    
for i in range(27):
    alphabetDict[alphabet[i]] = i
for i in range(len(initialString)):
    createdMatrix.append(alphabetDict[initialString[i]])
for i in range(len(createdMatrix)):
    if (i < len(createdMatrix)/2):
        encryptedMatrix.append((createdMatrix[i]*keyMatrix[0] + createdMatrix[i+len(createdMatrix)//2]*keyMatrix[1])%27)
    else:
        encryptedMatrix.append((createdMatrix[i-len(createdMatrix)//2]*keyMatrix[2] + createdMatrix[i]*keyMatrix[3])%27)

reversedAlphabetDict = {value : key for (key, value) in alphabetDict.items()}
for i in range(len(encryptedMatrix)):
    encryptedString = encryptedString + reversedAlphabetDict[encryptedMatrix[i]]

print(encryptedString)

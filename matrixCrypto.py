import numpy;

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

# BEGIN DECODE

print("second half!")

decryptString = "suuwxd esrkihpatsm"
decodeMatrix = [[4,5,12],[9,5,5],[13,13,7]]
decryptMatrix = []
linearInverse = []
answerMatrix = []
finalMatrix = []
output = ""

for j in range(3):
    temp = []
    for i in range(len(decryptString)//3):
        temp.append(alphabetDict[decryptString[i+(j*6)]])
    decryptMatrix.append(temp)
    temp.clear
    
decodeInverse = numpy.linalg.inv(decodeMatrix)
decodeInverse = decodeInverse * 514 # hardcoded GDC of inverted matrix

for i in decodeInverse:
    for j in range(len(i)):
        i[j] = i[j] % 27
        i[j] = int(round(i[j],0))
        linearInverse.append(int(i[j]))

intMatrix = []

for j in range(3):
    temp = []
    for i in range(3):
        temp.append(int(decodeInverse[j][i]))
    intMatrix.append(temp)
    temp.clear

answerMatrix = numpy.matmul(intMatrix, decryptMatrix)

for i in answerMatrix:
    for j in range(len(i)):
        i[j] = int(i[j] % 27)
        finalMatrix.append(reversedAlphabetDict[i[j]])

for i in range(len(finalMatrix)):
    output = output + finalMatrix[i]

print(output)
def generateAllStrings(inputString):
    stringCollection = []
    generateHelper(inputString, 0, "", stringCollection)
    return stringCollection

def generateHelper(inputString, index, currentString, stringCollection):
    if index == len(inputString):
        stringCollection.append(currentString)
    else:
        currentCharacter = inputString[index]
        if currentCharacter is int:
            generateHelper(inputString,index+1,currentString+currentCharacter, stringCollection)
        else:
            generateHelper(inputString,index+1,currentString+currentCharacter.lower(), stringCollection)
            generateHelper(inputString,index+1,currentString+currentCharacter.upper(), stringCollection)

print(generateAllStrings("abc"))
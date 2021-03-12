def runLengthEncoding(string):
	encodedStringCharacters = []
	currentRunLength = 1
	for i in range(1, len(string)):
		currentCharacter = string[i]
		previousCharacter = string[i-1]
		if currentCharacter != previousCharacter or currentRunLength ==9:
			encodedStringCharacters.append(str(currentRunLength))
			encodedStringCharacters.append(previousCharacter)
			currentRunLength = 0
		currentRunLength+=1
	encodedStringCharacters.append(str(currentRunLength))
	encodedStringCharacters.append(string[len(string)-1])
	return "".join(encodedStringCharacters)

result = runLengthEncoding("AAAAAAAAAAAAABBCCCCDD")
print("Input: AAAAAAAAAAAAABBCCCCDD")
print("Output: ", result)
if result == "9A4A2B4C2D":
    print("Test Case: Passsed")
else:
    print("Test Case: Failed")
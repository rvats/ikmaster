def runLengthEncoding(string):
    result = ""
    charCount = 0
    for index in range(len(string)-1):
        if charCount == 8:
            result+=str(charCount+1)+string[index]
            charCount = -1
        if string[index]!=string[index+1]:
            result+=str(charCount+1)+string[index]
            charCount=0
        else:
            charCount+=1
    result+=str(charCount+1)+string[len(string)-1]
    return result
result = runLengthEncoding("AAAAAAAAAAAAABBCCCCDD")
print("Input: AAAAAAAAAAAAABBCCCCDD")
print("Output: ", result)
if result == "9A4A2B4C2D":
    print("Test Case: Passsed")
else:
    print("Test Case: Failed")
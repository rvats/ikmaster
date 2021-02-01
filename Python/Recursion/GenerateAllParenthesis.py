def generateAllParenthesisDriver(number):
    generateAllParenthesisHelper(number, number, "")

def generateAllParenthesisHelper(remainingOpen, remainingClose, soFar):
    if remainingOpen > remainingClose:
        return
    if remainingOpen == 0 and remainingClose == 0:
        print(soFar)
    else:
        if  remainingOpen > 0:
            soFar+="("
            generateAllParenthesisHelper(remainingOpen-1, remainingClose, soFar)
            start, end = 0, len(soFar) - 1
            soFar[start:end]
        if remainingClose > 0:
            soFar+=")"
            generateAllParenthesisHelper(remainingOpen, remainingClose-1, soFar)
            start, end = 0, len(soFar) - 1
            soFar[start:end]

generateAllParenthesisDriver(2)

'''
(())
(()()
Press any key to continue . . .
'''
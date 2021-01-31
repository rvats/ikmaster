# Permutation Helper
def permutationHelper(dataCollected, inputSet):
    inputSetLength = len(inputSet)
    if inputSetLength == 0:
        print(dataCollected)
    else:
        for i in range(inputSetLength):
            dataAddedToCollection = inputSet[i]
            permutationHelper(dataCollected+dataAddedToCollection, inputSet[:i]+inputSet[i+1:])

inputSet = "abcd"
permutationHelper('', inputSet)

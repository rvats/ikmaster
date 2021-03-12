# Combination Helper Wrong Code
def combinationHelper(dataCollected, inputSet):
    inputSetLength = len(inputSet)
    if inputSetLength == 0:
        print(dataCollected)
    else:
        for i in range(inputSetLength):
            combinationHelper(dataCollected, inputSet[1:])
            dataCollected.append(inputSet[0])
            combinationHelper(dataCollected, inputSet[1:])
#inputSet = ["a","b","c","d"]
#inputSet = ["abcd"]
#inputSet = "abcd"
#combinationHelper([], inputSet)

# Function to create combinations without itertools 
def combinationGenerator(dataCollected, inputSet): 
    inputSetLength = len(inputSet)
    if inputSetLength == 0: 
        print(dataCollected)
    for i in range(inputSetLength): 
        combinationGenerator(dataCollected, inputSet[i + 1:])
        if(inputSet[i] not in dataCollected):
            dataCollected.append([inputSet[i]]) 
        combinationGenerator(dataCollected, inputSet[i + 1:])
# Driver code 
if __name__=="__main__": 
    arr ="abc"
    combinationGenerator([], [x for x in arr])
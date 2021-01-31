# Implementing PowerSet Problem Using Include Exclude Pattern
def powerSet(inputSet):
    powerSetCollection = []
    powerSetHelper(inputSet,0,[], powerSetCollection)
    return powerSetCollection

def powerSetHelper(inputSet, index, slate, powerSetCollection):
    if index == len(inputSet):
        print(slate)
        powerSetCollection.insert(len(powerSetCollection),slate[:])
    else:
        powerSetHelper(inputSet, index+1, slate, powerSetCollection)
        slate.append(inputSet[index])
        powerSetHelper(inputSet,index+1,slate, powerSetCollection)
        slate.pop()

print(powerSet(["1","2","3"]))
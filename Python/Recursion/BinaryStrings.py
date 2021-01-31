# BFS using O(n^2) Space Complexity
def binaryStringsMemo(n):
    if n == 1:
        return ["0","1"]
    else: # n >1
        prev = binaryStringsMemo(n-1)
        result = []
        for s in prev:
            result.append(s+"0")
            result.append(s+"1")
        return result

for binaryString in binaryStringsMemo(5):
    print(binaryString)

print("=======================================================================")

# DFS using O(n) Space Complexity
def binaryStringsOptimizedSpace(dataCollected, n):
    if n == 0:
        print(dataCollected)
    else: # n >1
        binaryStringsOptimizedSpace(dataCollected+"0", n-1)
        binaryStringsOptimizedSpace(dataCollected+"1", n-1)

binaryStringsOptimizedSpace("",5)

# BFS using O(n^2) Space Complexity
def decimalStringsMemo(n):
    if n == 1:
        return ["0","1","2","3","4","5","6","7","8","9"]
    else: # n >1
        prev = decimalStringsMemo(n-1)
        result = []
        for s in prev:
            for i in range(10):
                result.append(s+str(i))
        return result

for decimalString in decimalStringsMemo(2):
    print(decimalString)

print("=======================================================================")

# DFS using O(n) Space Complexity
def decimalStringsOptimizedSpace(dataCollected, n):
    if n == 0:
        print(dataCollected)
    else: # n >1
        for i in range(10):
            decimalStringsOptimizedSpace(dataCollected+str(i), n-1)

decimalStringsOptimizedSpace("",2)

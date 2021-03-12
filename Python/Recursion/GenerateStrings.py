# BFS using O(n^2) Space Complexity Wrong Solution
def stringsMemo(n, base):
    if n == 0:
        return [""]
    else: # n >1
        prev = stringsMemo(n-1, base)
        result = []
        for s in prev:
            for i in range(base):
                result.append(s+str(i))
        return result

print("=======================================================================")
print("Generating Binary Strings Using General StringsMemo")
for string in stringsMemo(2,2):
    print(string)
print("=======================================================================")
print("Generating Octal Strings Using General StringsMemo")
for string in stringsMemo(2,8):
    print(string)
print("=======================================================================")

# DFS using O(n) Space Complexity
def stringsOptimizedSpace(dataCollected, n, base):
    if n == 0:
        print(dataCollected)
    else: # n >1
        for i in range(base):
            stringsOptimizedSpace(dataCollected+str(i), n-1, base)
print("Generating Binary Strings Using General StringsOptimizedSpace")
stringsOptimizedSpace("",2,2)
print("=======================================================================")
print("Generating Octal Strings Using General StringsOptimizedSpace")
stringsOptimizedSpace("",2,8)
print("=======================================================================")
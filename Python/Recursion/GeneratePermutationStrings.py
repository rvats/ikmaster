# Permutation Helper with Hien Luu
def permutationHelper(input, index, slate):
    inputLength = len(input)
    if index == inputLength:
        print(slate)
    else:
        for i in range(index, inputLength):
            input[i], input[index] = input[index], input[i]
            slate.append(input[index])
            permutationHelper(input, index+1, slate)
            slate.pop()
            input[i], input[index] = input[index], input[i]

input = ["a","b","c", "d"]
permutationHelper(input,0,[])

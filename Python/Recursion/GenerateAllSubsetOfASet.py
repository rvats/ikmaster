# Program to print all subsets of a set given as an inputArray of size n 
def generateAllSubsetsOfASet(inputSet): 
    # A Temporary Array to store all subsets 
    data = [] 
    # Print all subsets using temporary array 'data[]' 
    start, end = 0, len(inputSet)-1
    for i in range(end):
        generateSubsetHelper(inputSet, data, 0, start, end, 0, i)
  
# inputSet ---> Input Array 
# data ---> Temporary array to store current combination 
# start & end ---> Staring and Ending indexes in inputSet[] 
# index ---> Current index in data[] 
# subSetLength ---> subsetLength 
def generateSubsetHelper(inputSet, data, start, end, index, subSetLength): 
    # Current combination is ready to be printed, print it 
    if (index == subSetLength): 
        for j in range(subSetLength): 
            print(data[j])
        print()
        return 
  
    # replace index with all 
    # possible elements. The 
    # condition "end-i+1 >=  
    # r-index" makes sure that  
    # including one element at 
    # index will make a combination  
    # with remaining elements at  
    # remaining positions 
    i = start;  
    while(i <= end and end - i + 1 >= subSetLength - index): 
        data[index] = arr[i]; 
        generateSubsetHelper(arr, data, i + 1,  
                        end, index + 1, subSetLength); 
        i += 1; 
  
# Driver Code 
inputSet = [1, 2, 3]; 
generateAllSubsetsOfASet(inputSet); 
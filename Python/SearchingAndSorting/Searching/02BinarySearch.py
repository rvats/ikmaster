class Search:
    # Binary Search is a simple searching algorithm which works on sorted data by searching from the middle of the data and moving to left if value to be search is less than middle element in data or right if its greater than value at the middle element by recursively searching for the data at the middle of the new section to search in.
    # numbers = 1, 2, 3, 4, 5, 6, 7, 8, 9 target = 2
    # start = 0 end = 8 mid = 4 numbers[mid] = 5
    # start = 0 end = 4 mid = 2 numbers[2] = 3
    # start = 0 end = 2 mid = 1 numbers[1] = 2 true
    # numbers = 1, 2, 3, 4, 5, 6, 7, 8, 9 target = 0
    # start = 0 end = 8 mid = 4 numbers[mid] = 5
    # start = 0 end = 4 mid = 2 numbers[2] = 3
    # start = 0 end = 2 mid = 1 numbers[1] = 2 
    # start = 0 end = 1 mid = 0 numbers[0] = 1
    # start = 0 end = 0 mid = 0 numbers[0] = 1 return false
    # numbers = 1, 3, 5, 7, 9 target = 4
    # start = 0 end = 4 mid = 2 numbers[mid] = 5
    # start = 0 end = 2 mid = 1 numbers[1] = 3
    # start = 1 end = 2 mid = 1 numbers[1] = 3
    # start = 1 end = 1 mid = 1 numbers[1] = 3 return false


    # Python3 code to implement iterative Binary Search.   
    # It returns location of x in given array arr  
    # if present, else returns -1 
    #@binarySearch
    def binarySearch(self, numbers, target): 
        start, end = 0, len(numbers)-1
        while start <= end: 
            mid = start + (end - start) // 2; 
            # Check if x is present at mid 
            if numbers[mid] == target: 
                return mid 
            # If x is greater, ignore left half 
            elif numbers[mid] < target: 
                start = mid + 1
            # If x is smaller, ignore right half 
            else: 
                end = mid - 1
        # If we reach here, then the element 
        # was not present 
        return -1

if __name__ == '__main__':
    print("Binary Search Demo")
    print("Searching 0 in [1,2,3,4,5,6,7,8,9]: Index: ",Search().binarySearch([1,2,3,4,5,6,7,8,9],0)," Found: ", Search().binarySearch([1,2,3,4,5,6,7,8,9],0)>=0)
    print("Searching 1 in [1,2,3,4,5,6,7,8,9]: Index: ",Search().binarySearch([1,2,3,4,5,6,7,8,9],1)," Found: ", Search().binarySearch([1,2,3,4,5,6,7,8,9],1)>=0)
    print("Searching 2 in [1,2,3,4,5,6,7,8,9]: Index: ",Search().binarySearch([1,2,3,4,5,6,7,8,9],2)," Found: ", Search().binarySearch([1,2,3,4,5,6,7,8,9],2)>=0)
    print("Searching 3 in [1,2,3,4,5,6,7,8,9]: Index: ",Search().binarySearch([1,2,3,4,5,6,7,8,9],3)," Found: ", Search().binarySearch([1,2,3,4,5,6,7,8,9],3)>=0)
    print("Searching 4 in [1,2,3,4,5,6,7,8,9]: Index: ",Search().binarySearch([1,2,3,4,5,6,7,8,9],4)," Found: ", Search().binarySearch([1,2,3,4,5,6,7,8,9],4)>=0)
    print("Searching 5 in [1,2,3,4,5,6,7,8,9]: Index: ",Search().binarySearch([1,2,3,4,5,6,7,8,9],5)," Found: ", Search().binarySearch([1,2,3,4,5,6,7,8,9],5)>=0)
    print("Searching 6 in [1,2,3,4,5,6,7,8,9]: Index: ",Search().binarySearch([1,2,3,4,5,6,7,8,9],6)," Found: ", Search().binarySearch([1,2,3,4,5,6,7,8,9],6)>=0)
    print("Searching 7 in [1,2,3,4,5,6,7,8,9]: Index: ",Search().binarySearch([1,2,3,4,5,6,7,8,9],7)," Found: ", Search().binarySearch([1,2,3,4,5,6,7,8,9],7)>=0)
    print("Searching 8 in [1,2,3,4,5,6,7,8,9]: Index: ",Search().binarySearch([1,2,3,4,5,6,7,8,9],8)," Found: ", Search().binarySearch([1,2,3,4,5,6,7,8,9],8)>=0)
    print("Searching 9 in [1,2,3,4,5,6,7,8,9]: Index: ",Search().binarySearch([1,2,3,4,5,6,7,8,9],9)," Found: ", Search().binarySearch([1,2,3,4,5,6,7,8,9],9)>=0)
    print("Searching 10 in [1,2,3,4,5,6,7,8,9]: Index: ",Search().binarySearch([1,2,3,4,5,6,7,8,9],10)," Found: ", Search().binarySearch([1,2,3,4,5,6,7,8,9],10)>=0)
    print("Searching 0 in [1,3,5,7,9]: Index: ",Search().binarySearch([1,3,5,7,9],0)," Found: ", Search().binarySearch([1,3,5,7,9],0)>=0)
    print("Searching 1 in [1,3,5,7,9]: Index: ",Search().binarySearch([1,3,5,7,9],1)," Found: ", Search().binarySearch([1,3,5,7,9],1)>=0)
    print("Searching 2 in [1,3,5,7,9]: Index: ",Search().binarySearch([1,3,5,7,9],2)," Found: ", Search().binarySearch([1,3,5,7,9],2)>=0)
    print("Searching 3 in [1,3,5,7,9]: Index: ",Search().binarySearch([1,3,5,7,9],3)," Found: ", Search().binarySearch([1,3,5,7,9],3)>=0)
    print("Searching 4 in [1,3,5,7,9]: Index: ",Search().binarySearch([1,3,5,7,9],4)," Found: ", Search().binarySearch([1,3,5,7,9],4)>=0)
    print("Searching 5 in [1,3,5,7,9]: Index: ",Search().binarySearch([1,3,5,7,9],5)," Found: ", Search().binarySearch([1,3,5,7,9],5)>=0)
    print("Searching 6 in [1,3,5,7,9]: Index: ",Search().binarySearch([1,3,5,7,9],6)," Found: ", Search().binarySearch([1,3,5,7,9],6)>=0)
    print("Searching 7 in [1,3,5,7,9]: Index: ",Search().binarySearch([1,3,5,7,9],7)," Found: ", Search().binarySearch([1,3,5,7,9],7)>=0)
    print("Searching 8 in [1,3,5,7,9]: Index: ",Search().binarySearch([1,3,5,7,9],8)," Found: ", Search().binarySearch([1,3,5,7,9],8)>=0)
    print("Searching 9 in [1,3,5,7,9]: Index: ",Search().binarySearch([1,3,5,7,9],9)," Found: ", Search().binarySearch([1,3,5,7,9],9)>=0)
    print("Searching 10 in [1,3,5,7,9]: Index: ",Search().binarySearch([1,3,5,7,9],10)," Found: ", Search().binarySearch([1,3,5,7,9],10)>=0)
    
class Search:
    # Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.

    #@linearSearch
    def linearSearch(self, numbers, target):
        n = len(numbers) 
        # Traverse through all array elements 
        for i in range(n): 
            if(numbers[i]==target):
                return i
        return -1

if __name__ == '__main__':
    print("Linear Search Demo")
    print("Searching 0 in [1,3,5,7,9]: Found at Index: ",Search().linearSearch([1,3,5,7,9],0)," Found: ", Search().linearSearch([1,3,5,7,9],0)>=0)
    print("Searching 1 in [1,3,5,7,9]: Found at Index: ",Search().linearSearch([1,3,5,7,9],1)," Found: ", Search().linearSearch([1,3,5,7,9],1)>=0)
    print("Searching 2 in [1,3,5,7,9]: Found at Index: ",Search().linearSearch([1,3,5,7,9],2)," Found: ", Search().linearSearch([1,3,5,7,9],2)>=0)
    print("Searching 3 in [1,3,5,7,9]: Found at Index: ",Search().linearSearch([1,3,5,7,9],3)," Found: ", Search().linearSearch([1,3,5,7,9],3)>=0)
    print("Searching 4 in [1,3,5,7,9]: Found at Index: ",Search().linearSearch([1,3,5,7,9],4)," Found: ", Search().linearSearch([1,3,5,7,9],4)>=0)
    print("Searching 5 in [1,3,5,7,9]: Found at Index: ",Search().linearSearch([1,3,5,7,9],5)," Found: ", Search().linearSearch([1,3,5,7,9],5)>=0)
    print("Searching 6 in [1,3,5,7,9]: Found at Index: ",Search().linearSearch([1,3,5,7,9],6)," Found: ", Search().linearSearch([1,3,5,7,9],6)>=0)
    print("Searching 7 in [1,3,5,7,9]: Found at Index: ",Search().linearSearch([1,3,5,7,9],7)," Found: ", Search().linearSearch([1,3,5,7,9],7)>=0)
    print("Searching 8 in [1,3,5,7,9]: Found at Index: ",Search().linearSearch([1,3,5,7,9],8)," Found: ", Search().linearSearch([1,3,5,7,9],8)>=0)
    print("Searching 9 in [1,3,5,7,9]: Found at Index: ",Search().linearSearch([1,3,5,7,9],9)," Found: ", Search().linearSearch([1,3,5,7,9],9)>=0)
    print("Searching 10 in [1,3,5,7,9]: Found at Index: ",Search().linearSearch([1,3,5,7,9],10)," Found: ", Search().linearSearch([1,3,5,7,9],10)>=0)
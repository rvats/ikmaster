def check_if_sum_possible(arr, k):
    lookup = {}
    return check_if_sum_possible_helper(arr, len(arr), k, lookup)

def check_if_sum_possible_helper(arr, n, sum, lookup):
    if (len(lookup)>0 and sum == 0):
        return True
    if n < 0 or sum < 0:
        return False
    key = (n, sum)
    
    if key not in lookup:
        include = check_if_sum_possible_helper(arr, n - 1, sum - arr[n], lookup)
        exclude = check_if_sum_possible_helper(arr, n - 1, sum, lookup)
        lookup[key] = include or exclude
    return lookup[key]
 
 
# Driver code
set = [1]
sum = 0
if (check_if_sum_possible(set, sum) == True):
    print("Found a subset with given sum")
else:
    print("No subset with given sum")
def check_if_sum_possible(arr, k):

    result = []
    def back_track(i,sum,currentSet):
        # backtracking case
        if i == len(arr):
            if sum == k and len(currentSet) > 0:
                result.append(True)
        elif i < len(arr):
            back_track(i + 1, sum,currentSet)
            currentSet.append(arr[i])
            back_track(i + 1, sum+arr[i],currentSet)
            currentSet.pop()
    back_track(0,0,[])
    return True in result

print(check_if_sum_possible([1],0))
print(check_if_sum_possible([2,4,8],6))
print(check_if_sum_possible([2,4,8],5))
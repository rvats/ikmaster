class Solution:
    def subsetsWithDup(self, nums):
        powerset = []
        
        def subsetsWithDupHelper(nums, powerset, subset, index):
            if index == len(nums):
                if subset not in powerset:
                    powerset.append(subset[:])
            else:

                subsetsWithDupHelper(nums, powerset, subset, index + 1)
                subset.append(nums[index])
                subsetsWithDupHelper(nums, powerset, subset, index + 1)
                subset.pop()
            return powerset
            
        subsetsWithDupHelper(nums, powerset, [], 0)
        return powerset

print(Solution().subsetsWithDup([0,1,1]))
'''
341. Flatten Nested List Iterator
https://leetcode.com/problems/flatten-nested-list-iterator/
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.
Implement the NestedIterator class:
NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
int next() Returns the next integer in the nested list.
boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.
Your code will be tested with the following pseudocode:
initialize iterator with nestedList
res = []
while iterator.hasNext()
    append iterator.next() to the end of res
return res
If res matches the expected flattened list, then your code will be judged as correct.
Example 1:
Input: nestedList = [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].
Example 2:
Input: nestedList = [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].
Constraints:
1 <= nestedList.length <= 500
The values of the integers in the nested list is in the range [-106, 106]
To solve the problem:
Using Peeking Iterator Pattern.  
I am using generators as described in https://realpython.com/introduction-to-python-generators/ Python yield generators
I forgot the yield next in the interview scenario. Note to self: Do not make this mistake and brush up on your syntax especially if you have not been using the language of choice for interview in a while.
Another approach could be to use stacks
'''
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """

#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator:

    def __init__(self, nestedList: [NestedInteger]):
        self.list = self.GenerateList(nestedList)
        self.peeked = None # Keep Tracked of the topmost/frontmost integer

    def GenerateList(self, nestedList):
        for item in nestedList:
            if item.isInteger():
                yield item.getInteger()
            else:
                yield from self.GenerateList(item.getList())
    
    def GetNext(self) -> int: # Change the name to what was in problem statement
        if not self.HasNext(): 
            return None
        next, self.peeked = self.peeked, None
        return next
        
    def HasNext(self) -> bool: # Change the name to what was in problem statement
        if self.peeked is not None: 
            return True
        try: 
            self.peeked = next(self.list) # Forgot the syntax in python and was thinking it will be the function that we are writing for getting next. Hence the confusion with circular loop. This code works as tested. 
            return True
        except: 
            return False
# Test Case 1: 
## [1,[2,[3,4,[5,6]]]]
nestedInteger1 = NestedInteger(1)
nestedInteger2 = NestedInteger(2)
nestedInteger3 = NestedInteger(3)
nestedInteger4 = NestedInteger(4)
nestedInteger5 = NestedInteger(5)
nestedInteger6 = NestedInteger(6)

nestedList = [nestedInteger1, [nestedInteger2, [nestedInteger3, nestedInteger4, [nestedInteger5, nestedInteger6]]]]

i, v = NestedIterator(nestedList), []
while i.HasNext(): 
    v.append(i.GetNext())
print(v)

'''
Approach using stacks
'''
# Second Approach with stacks
class NestedIterator2:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = nestedList[::-1]
        self.findNextInteger()
    
    def findNextInteger(self):
        # make sure the top of the stack is an integer
        # i.e: self.stack.top().isInteger() == True
        while len(self.stack) > 0 and not self.stack[-1].isInteger():
            # get the list
            l = self.stack.pop().getList()
            while len(l) > 0:
                self.stack.append(l.pop())
    
    def next(self) -> int:
        res = self.stack.pop()
        self.findNextInteger()
        return res.getInteger()
    
    def hasNext(self) -> bool:
        return len(self.stack) > 0
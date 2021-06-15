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
        self.list = self.generateList(nestedList)
        self.peeked = None

    def generateList(self, nestedList):
        for item in nestedList:
            if item.isInteger():
                yield item.getInteger()
            else:
                yield from self.generateList(item.getList())
    
    def next(self) -> int:
        if not self.hasNext(): 
            return None
        next, self.peeked = self.peeked, None
        return next
        
    def hasNext(self) -> bool:
        if self.peeked is not None: 
            return True
        try: 
            self.peeked = next(self.list)
            return True
        except: 
            return False
        
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

# Test Run of my code: 
## Accepted
## Runtime: 48 ms
## Your input
## [1,[2,[3,4,[5,6]]]]
## Output
## [1,2,3,4,5,6]
## Expected
## [1,2,3,4,5,6]
## Success
## Details 
## Runtime: 64 ms, faster than 82.24% of Python3 online submissions for Flatten Nested List Iterator.
## Memory Usage: 17.8 MB, less than 39.09% of Python3 online submissions for Flatten Nested List Iterator.
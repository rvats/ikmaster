"""
# == == == == == == == == == == == == == == == == == == == == == =
#
# Write a function to generate the generalized abbreviations of a word.
#
# Example:
#
# Input: "word"
# Output:
# [
#   "word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2",
#   "1o1d", "1or1", "w1r1",
#   "1o2", "2r1", "3d", "w3", "4"
#  ]
# Input: "aaa"
# Output: 
["3","2a","1a1","1aa","a2","a1a","aa1","aaa"]
#
                ======================
                    aaa
            change nothing 0: aaa        
            Change 1 Character at a time: 1aa a1a aa1
            Change 1 Character at each alternate character positon but more than 1 instance: 1a1
            
            Change 2 character at a time: 2a a2
            ...
            Change all n characters in string: n
            ======================
                    word
            0: word
            1 for 1 character: 1ord, w1rd, wo1d, wor1
            ======================
                    aaaaa
            1 character at alternate location: 1a1a1, a1a1a  aa1a1 a1aa1 
            BaseCase string is of length n
            idx == n 
                collection.append(slate) S.C. leaving out output, there will callstack will be taking memory 
                        idx = O(1) Slate O(n)
                T.C = O (2^n)
            else: 
            for i in range (0,idx)
                helper(string, idx+1, slate+1)
                helper(string, idx+2, slate+1)
            
# == == == == == == == == == == == == == == == == == == == == == =
["5","4a","3a1","3aa","2a2","2a1a","2aa1","2aaa","1a3","1a2a","1a1a1","1a1aa","1aa2","1aa1a","1aaa1","1aaaa","a4","a3a","a2a1","a2aa","a1a2","a1a1a","a1aa1","a1aaa","aa3","aa2a","aa1a1","aa1aa","aaa2","aaa1a","aaaa1","aaaaa"]

"""

def generateAllAbbreviations(string):
    aC = []
    def helper(string, idx, slate, aC):
        if idx > len(string)-1:
            return 
        if idx == len(string):
            #print(slate)
            aC.append(slate)
        else: 
            for i in range(0, idx):
                helper(string, i+1, slate+string[0:i+1], aC) # aaa
                helper(string, i+1, slate+str(i+1), aC)  # aa1, a1a, 1aa, 2aa
    helper(string, 0, "", aC)
    return aC

#print(generateAllAbbreviations("a"))
print(generateAllAbbreviations("aa"))
            
class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        def back_track(i, count):
            # base
            if i >= len(word):
                if count: temp.append(str(count))
                res.append(''.join(temp[:]))
                if count: temp.pop()
                return

            # rec
            # exclude: abbreviate current char
            back_track(i + 1, count + 1)
            # include: record count and current char
            if count: temp.append(str(count))
            temp.append(word[i])
            back_track(i + 1, 0)  # reset abbreviation count
            temp.pop()
            if count: temp.pop()

        temp, res = [], []
        back_track(0, 0)
        return res            
            
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def back_track(i):
            # backtracking case
            if i == len(nums):
                res.append(temp[:])
                return

            # rec case
            # exclude
            back_track(i + 1)
            # include
            temp.append(nums[i])
            back_track(i + 1)
            temp.pop()

        temp, res = [], []
        back_track(0)
        return res            
            
            
            
            
            
            
            
            
            
            
            
            
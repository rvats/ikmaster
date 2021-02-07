'''
320. Generalized Abbreviation
A word's generalized abbreviation can be constructed by taking any number of non-overlapping substrings and replacing them with their respective lengths. For example, "abcde" can be abbreviated into "a3e" ("bcd" turned into "3"), "1bcd1" ("a" and "e" both turned into "1"), and "23" ("ab" turned into "2" and "cde" turned into "3").
Given a string word, return a list of all the possible generalized abbreviations of word. Return the answer in any order.
Example 1: Input: word = "word"
Output: ["4","3d","2r1","2rd","1o2","1o1d","1or1","1ord","w3","w2d","w1r1","w1rd","wo2","wo1d","wor1","word"]
Example 2: Input: word = "a"
Output: ["1","a"]
Constraints:
1 <= word.length <= 15
word consists of only lowercase English letters.
'''
class Solution:
    def generateAbbreviations(self, word):
        collection, temp = [], []
        def helper(idx, count):
            if idx >= len(word):
                if count: 
                    temp.append(str(count))
                collection.append(''.join(temp[:]))
                if count: 
                    temp.pop()
                return
            elif idx < len(word):
                helper(idx+1,count+1)
                if count: 
                    temp.append(str(count))
                temp.append(word[idx])
                helper(idx+1,0)
                temp.pop()
                if count: 
                    temp.pop()            
        helper(0,0)
        return collection

print(Solution().generateAbbreviations("a"))
print("==========================================================================================")
print(Solution().generateAbbreviations("aa"))
print("==========================================================================================")
print(Solution().generateAbbreviations("aaa"))
print("==========================================================================================")
print(Solution().generateAbbreviations("word"))
print("==========================================================================================")
'''
https://leetcode.com/problems/interleaving-string/
97. Interleaving String
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:
s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.
Example 1:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
'''
def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    if len(s1) + len(s2) != len(s3):
        return False
    ilMap = [[False for row in range(len(s1)+1)] for col in range(len(s2)+1)]
    for s1idx in range(len(s1)+1):
        for s2idx in range(len(s2)+1):
            ilMap[s1idx][s2idx] = (s1idx == 0 and s2idx ==0) or (s1idx > 0 and ilMap[s1idx-1][s2idx] and s1[s1idx]==s3[s1idx+s2idx]) or (s2idx > 0 and ilMap[s1idx][s2idx-1] and s2[s2idx]==s3[s1idx+s2idx])
    return ilMap[len(s1)][len(s2)]
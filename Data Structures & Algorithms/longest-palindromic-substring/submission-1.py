class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        # keep left and rigt ptrs
        # keep advancing right until it reaches end 
        # each time it forms a palindrome, res = max(curr, res)
        # advnce left
        for l in range (len(s)):
            for r in range(l + 1, len(s) + 1):
                subS = s[l:r]
        
                if subS == subS[::-1] and len(subS) > len(res):
                    res = subS
        
        return res
                
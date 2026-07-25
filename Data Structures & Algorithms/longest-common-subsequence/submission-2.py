class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # at a given idx, you can choose whether to include it or not in curr subsequence
        # solve recursively, and you explore both options and take max. length
        # each recursive calls solves max subseq from text1[i:] and text2[j:]
        #   so we first call dfs(0,0) as our final soln because its  whole stinrg
        # per call, if the i and j chars match then we should include it, otherwise we skip and advance either i or j
        # base case: in memo OR i == len(text1) or j == len(text2)
        
        memo = {} 
        
        # returns longest subseq. found from text1[i:] and text2[j:]
        def dfs(i, j):
            if i == len(text1) or j == len(text2):
                return 0

            if (i, j) in memo:
                return memo[(i,j)]
            
            # match found
            #   advance to next char of text1
            #   adjust search space of text2
            if text1[i] == text2[j]:
                memo[(i,j)] = dfs(i + 1, j + 1) + 1
            # skip curr char of text1 or text2
            else:
                memo[(i,j)] = max(dfs(i+1, j), dfs(i, j+1))
    
            return memo[(i,j)]

        return dfs(0,0)
            

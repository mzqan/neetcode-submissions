class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # recursion: dfs(0, 0, 0) for final soln
        #   dfs(i,j,k) represents if s1[i:] and s2[j:] can form s3[k:]
        #   at each call, we include s1 (if s1[i] == s3[k] and i in bounds) and s2 (if s2[j] == s3[k] and j in bounds), advancing i/j and k as needed
        #                 if including s1 OR s2 is valid (by default false), then we set memo[(i,j,k)] as true.
        #   base case: s1 and s2 ran out

        # cannot interleave , not right amt of chars
        if len(s1) + len(s2) != len(s3):
            return False
            
        memo = {}

        def dfs(i,j,k):
            # ran out of chars to evalute in s1/s2
            if i == len(s1) and j == len(s2):
                # interleaved all of s3
                return k == len(s3)
            
            if (i,j,k) in memo:
                return memo[(i,j,k)]

            include1 = dfs(i + 1, j, k + 1) if (i < len(s1) and s1[i] == s3[k]) else False
            include2 = dfs(i, j + 1, k + 1) if (j < len(s2) and s2[j] == s3[k]) else False

            memo[(i,j,k)] = include1 or include2

            return memo[(i,j,k)]
        
        return dfs(0,0,0)
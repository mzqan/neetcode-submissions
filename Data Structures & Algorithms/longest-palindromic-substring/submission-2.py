class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        resIdx, resLen = 0, 0

        dp = [[False] * n for _ in range(n)]
        

        # create 2D table, dp[i][j] for s[i:j+1]
        # if s[i] == s[j], and dp[i-1][j] then its also a substring

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and ((j - i <= 2) or dp[i+1][j-1]):
                    dp[i][j] = True
                    if (j - i + 1) > resLen:
                        resIdx = i
                        resLen = j - i + 1

        return s[resIdx : resIdx + resLen]
                
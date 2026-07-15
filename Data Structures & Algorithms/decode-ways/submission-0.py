class Solution:
    def numDecodings(self, s: str) -> int:
        memo = [0] * len(s)

        # to know dp[i+1], like dp[i] and dp[i-2] (except leading zeros)
        # at idx i = 0:
        #   add to memo, memo[i] = 1
        # at idx i = 1:
        #   add to memo, memo[i] = 2          
        # at idx i > 1:
        #   add to memo, memo[i] = 1 + memo[i-1]
        #               if i-1 != 0, memo[i] += 1 + memo[i-2]

        for i in range (len(s)):
            c = s[i]
            if i == 0 and c != '0':
                memo[i] = 1
            elif i > 0:
                # 0 is not valid
                if c != '0':
                    memo[i] = memo[i-1]

                # not leading zero AND within A-Z range
                pair = int(s[i-1:i+1])
                if pair > 9 and pair < 27:
                    memo[i] += memo[i-2] if i > 1 else 1
        
        return memo[-1]


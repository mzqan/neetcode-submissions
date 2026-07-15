class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {0: 0}

        def minAmount(target):
            if target in memo:
                return memo[target]
            
            best = float('inf')
            for c in coins:
                left = target - c
                if left >= 0:
                    best = min(best, minAmount(left) + 1)
            
            memo[target] = best
            return memo[target]
        
        minAmount(amount)

        return memo[amount] if memo[amount] != float('inf') else -1
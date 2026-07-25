class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # on each day, you can choose to either buy, sell or skip
        # recursion on dfs(0, false) for final soln
        #   dfs(i, holding) represents max. profit from day[i:] if you're holding a Neetcoin or not
        #   on each call, we explore 3 options to get max of buy (if !holding), sell (advance i twice b/c you can't buy again), or skip (advance i)
        #   after you buy, you can store
        #   base case: i == len(prices)
        
        memo = {}
        def dfs(i, holding):
            if i >= len(prices):
                return 0
            
            if (i, holding) in memo:
                return memo[(i, holding)]

            buy = sell = 0
            if not holding:
                buy = dfs(i + 1, True) - prices[i]
            if holding:
                sell = dfs(i + 2, False) + prices[i]

            skip = dfs(i+1, holding)
            memo[(i, holding)] = max(buy, sell, skip)

            return memo[(i, holding)]
            
        return dfs(0, False)


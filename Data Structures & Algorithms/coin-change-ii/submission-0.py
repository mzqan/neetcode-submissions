class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # top down
        # recursion: we call dfs(i, amount) for final soln
        #   dfs(i, amt) represents the number of ways to form amt with coins[i:]
        #   we want unique combinations, so   
        # at each call, we iterate through coins to test either advancing coin[i] or not
        #       if next call is non zero, then it was valid -> increment curr
        #   we memoize memo[amt] = curr to remember solns
        #   base case: amt < 0 return 0, amt == 0 return 1
        memo = {}

        def dfs(i, amt):
            # invalid soln, took took much/negative OR nothing else to choose form
            if amt < 0 or i >= len(coins):
                return 0

            # valid soln, aka don't pick anything
            if amt == 0:
                return 1

            if (i, amt) in memo:
                return memo[(i,amt)]

            # keep coin and maintain search space OR skip and advance search space
            memo[(i, amt)] = dfs(i, amt-coins[i]) + dfs(i+1, amt)

            return memo[(i, amt)]
    
        return dfs(0, amount)
            



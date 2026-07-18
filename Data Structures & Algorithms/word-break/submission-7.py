class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # recursion passing idx start
        # foo: True if s[start:] can be broken into words, False otherwise
        # base case: start == len(s) + 1, return
        # in each call, we loop from start -> end..
        # if s[start:end] is True then call foo(end)..
        # we memoize s[start]
        # if res is still False, let's 
        memo = {}
        ref = set(wordDict)

        def foo(start):
            if start in memo:
                return memo[start]

            if start == len(s):
                return True

            res = False
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in ref and foo(end):
                    res = True
                    break
            
            memo[start] = res
            return res
                    
        return foo(0)


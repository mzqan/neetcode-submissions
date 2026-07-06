class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        mapping = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}
        res = []
        curr = []

        # have a mapping
        # backtrack keeps track of current idx of digits
        # in each backtrack we loop thru posisble values of that digit
        # base case: idx > len(digits)

        def backtrack(i):
            nonlocal curr, res

            if i == len(digits):
                res.append("".join(curr))
                return

            for letter in mapping[digits[i]]:
                curr.append(letter)
                backtrack(i+1)
                curr.pop()
            
        backtrack(0)
        return res

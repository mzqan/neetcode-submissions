class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # backtrack
        # add a open or add a closed decision
        # can only add a closed if there's enough opened already placed
        # base case: no moreclosed can be added

        res = []
        curr = []

        def backtrack(o, c):
            if o == 0 and c == 0:
                res.append("".join(curr))
                return

            # add open
            if o:
                curr.append("(")
                backtrack(o - 1, c)
                curr.pop()

            # add closed, if possible
            if c > o:
                curr.append(")")
                backtrack(o, c - 1)
                curr.pop()

        backtrack(n, n)
        return res


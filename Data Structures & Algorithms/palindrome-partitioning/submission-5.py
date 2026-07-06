class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []

        # backtrack
        # determine indices to slice
        # if r indice is end of s, then push to. res

        def backtrack(start):
            nonlocal res, curr
            if start == len(s):
                res.append(curr.copy())
                return

            for i in range(start + 1, len(s) + 1):
                subS = s[start:i]
                if subS == subS[::-1]:
                    curr.append(subS)
                    backtrack(i)
                    curr.pop()                
  
        backtrack(0)

        return res
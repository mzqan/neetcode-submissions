class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []

        # backtrack
        # determine indices to slice
        # if r indice is end of s, then push to. res

        def backtrack(l, r):
            nonlocal res, curr
            if r == len(s):
                if r > l and s[l:r] == s[l:r][::-1]:
                    curr.append(s[l:r])
                    res.append(curr.copy())
                    curr.pop()
                return

            # if palindrome, "include" path
            if s[l:r] == s[l:r][::-1]:
                curr.append(s[l:r])
                backtrack(r, r+1)
                curr.pop()

            # keep adding
            if r < len(s):
                backtrack(l, r+1)
            

  
        backtrack(0, 1)

        return res
class Solution:
    def checkValidString(self, s: str) -> bool:
        # keep track of curr encountered LEFTs, idx
        # if we encounter a right, decrement curr lefts (unless there's none AND no stars, it's invalid)
        # if we encounter a star, we remebver it's idx
        # at end, if there's too many lefts then we see if any stars would help
        # ( ( * ) 

        lefts = []
        stars = []

        for i, c in enumerate(s):
            if c == '(':
                lefts.append(i)
                continue
            if c == '*':
                stars.append(i)
                continue

            if lefts:
                lefts.pop()
            elif stars:
                stars.pop()
            else:
                return False

        while lefts:
            if stars and lefts[-1] < stars[-1]:
                lefts.pop()
                stars.pop()
            else: 
                return False
            
        return True

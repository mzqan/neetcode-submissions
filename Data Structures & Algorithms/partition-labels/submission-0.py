class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ref = {} # stores last idx seen with num
        for i, c in enumerate(s):
            ref[c] = i

        # keep iterating idx until end
        # we remember what curr window end should be, keep updating as we find new chars
        res = []
        prevJumpEnd = -1
        currJumpEnd = -1

        for i, c in enumerate(s):
            # update window's min. end 
            currJumpEnd = max(currJumpEnd, ref[c])

            if i == currJumpEnd:
                res.append(currJumpEnd - prevJumpEnd)
                prevJumpEnd = currJumpEnd

        return res

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        curr = []

        def backtrack(i, currSum):
            if currSum == target:
                res.append(curr.copy())
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue

                if (candidates[j] + currSum) <= target:
                    curr.append(candidates[j])
                    backtrack(j + 1, currSum + candidates[j])
                    curr.pop()

        backtrack(0, 0)
        return res
                
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # update a triplet by taking max of (a,b,c) its current and another new
        # dont take a triplet if a,b,c > target's

        curr = [0, 0, 0] 
        a, b, c = target

        for triplet in triplets:
            if triplet[0] > a or triplet[1] > b or triplet[2] > c:
                continue
            
            curr = [max(curr[0], triplet[0]), max(curr[1], triplet[1]), max(curr[2], triplet[2])]
        
        return curr == target
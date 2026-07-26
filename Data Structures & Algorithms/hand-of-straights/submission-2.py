class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # if hand not divisble by groupSize , return
        if len(hand) % groupSize:
            return False
        
        # frequency
        freq = {}
        for card in hand:
            freq[card] = freq.get(card, 0) + 1
        
        for card in sorted(freq.keys()):
            count = freq[card]
            
            if count <= 0:
                continue

            for i in range(groupSize):
                if freq.get(card + i, -1) >= count:
                    freq[card + i] -= count
                else:
                    return False
            
            if freq[card]:
                return False

        return True 
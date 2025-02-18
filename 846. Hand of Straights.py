# 846. Hand of Straights
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        hand.sort()
        cur = hand[0]
        hand.remove(cur)
        counter = 1
        while hand:
            if counter == groupSize:
                cur = hand[0] 
                counter = 1
                hand.remove(cur)
            elif cur + 1 in hand:
                counter += 1
                cur += 1
                hand.remove(cur)
            else:
                return False
        return True
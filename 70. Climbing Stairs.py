class Solution:
    def climbStairs(self, n: int) -> int:
        p1, p2 = 1, 1 
        while n > 1:
            tmp = p2
            p2 = p2 + p1
            p1 = tmp
            n -= 1 
        
        return p2
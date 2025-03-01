# 202. Happy Number
class Solution:
    def isHappy(self, n: int) -> bool: 
        visited = set()
        while True:
            if n == 1:
                return True
            if n in visited:
                return False

            k = 0
            for s in str(n):
                s = int(s)
                k += s ** 2
            visited.add(n)
            n = k

# 50. Pow(x, n)
class Solution:
    def myPow(self, x: float, n: int) -> float:

        def rec_pow(x, n): 
            if x == 0:
                return 0
            if n == 0:
                return 1
            if n == 1:
                return x
            
            res = rec_pow(x, n // 2)
            res = res * res

            return res * x if n % 2 else res


        res = rec_pow(x, abs(n))
        return res if n > 0 else 1 / res
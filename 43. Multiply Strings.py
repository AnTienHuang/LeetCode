# 43. Multiply Strings
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        res = [0] * (len(num1) + len(num2))
        num1 = num1[::-1]
        num2 = num2[::-1]

        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                i = i1 + i2
                v = int(num1[i1]) * int(num2[i2]) + res[i]
                carry = v // 10
                res[i] = v % 10
                while carry:
                    tmp = res[i + 1] + carry
                    res[i + 1] = tmp % 10
                    carry = tmp // 10
                    i += 1
        
        while res[-1] == 0:
            res.pop()

        return "".join(str(r) for r in res[::-1])
                

                
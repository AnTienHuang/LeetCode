# 66. Plus One
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = len(digits) - 1

        while carry:
            carry -= 1
            if digits[i] == 9:
                if i == 0:
                    digits[i] = 0
                    digits.insert(0, 1)
                else:
                    digits[i] = 0
                    carry += 1
                    i -= 1
            else:
                digits[i] += 1
        
        return digits
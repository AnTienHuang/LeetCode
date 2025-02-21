# 678. Valid Parenthesis String
class Solution:
    def checkValidString(self, s: str) -> bool:
        min_left = 0 # Treating * as ) or space
        max_left = 0 # Treating * as (

        for c in s:
            if c == "(":
                min_left += 1
                max_left += 1
            elif c == ")":
                min_left -= 1
                max_left -= 1
            else: # c == "*"
                min_left -= 1
                max_left += 1

            if min_left < 0:
                min_left = 0

            if max_left < 0:
                return False
            
        return min_left == 0

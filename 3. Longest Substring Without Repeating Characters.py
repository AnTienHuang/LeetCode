# 3. Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1

        l, r = 0, 1
        res = 0

        while r < len(s):
            while r > l and s[r] in s[l:r]:
                l += 1
            res = max(res, r - l + 1)
            r += 1
        
        return res
        
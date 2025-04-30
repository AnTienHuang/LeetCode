# 424. Longest Repeating Character Replacement
class Solution:
    def characterReplacement(self, s: str, k: int) -> int: 
        res = 0
        max_frequency = 0
        l = 0
        r = 0
        window = {}
        while r < len(s):
            window[s[r]] = 1 + window.get(s[r], 0)
            if window[s[r]] > max_frequency:
                max_frequency = window[s[r]]
            if r - l + 1 - max_frequency <= k:
                res = max(res, r - l + 1)
            while r - l + 1 - max_frequency > k:
                window[s[l]] -= 1
                l += 1
            r += 1
        
        return res
    
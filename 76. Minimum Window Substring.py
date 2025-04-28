# 76. Minimum Window Substring
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return "" 
        count = {}
        for char in t:
            count[char] = 1 + count.get(char, 0)
        start, end = -1, len(s)
        l = 0
        while l <= len(s) - len(t):
            while l + 1 < len(s) and s[l] not in count:
                l += 1
            count_copy = count.copy()
            r = l
            match = len(t)
            while match > 0 and r < len(s) - 1:
                if s[r] in count_copy and count_copy[s[r]] > 0:
                    count_copy[s[r]] -= 1
                    match -= 1
                r += 1
            if match == 0:
                if end - start > r - l:
                    end = r
                    start = l
            l += 1

        return "" if start == -1 else s[start : end + 1]

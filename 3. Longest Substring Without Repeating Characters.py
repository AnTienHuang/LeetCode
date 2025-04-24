# 3. Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2: return len(s)
        res = 0
        cache = [s[0]]
        l, r = 0, 1
        while r < len(s):
            while s[r] in cache:
                cache.remove(s[l])
                l += 1
            cache.append(s[r])
            res = max(res, r - l + 1)
            r += 1
        return res

    # 1st attempt
    #     if len(s) == 1:
    #         return 1

    #     l, r = 0, 1
    #     res = 0

    #     while r < len(s):
    #         while r > l and s[r] in s[l:r]:
    #             l += 1
    #         res = max(res, r - l + 1)
    #         r += 1
        
    #     return res
        
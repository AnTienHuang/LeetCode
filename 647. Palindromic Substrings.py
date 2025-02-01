class Solution:
    def countSubstrings(self, s: str) -> int:
        res = []

        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res.append(s[l:r + 1])
                l -= 1
                r += 1
            
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res.append(s[l:r + 1])
                l -= 1
                r += 1

        return len(res)
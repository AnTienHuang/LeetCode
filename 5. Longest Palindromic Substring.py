class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = 0
        pali = s[0] # keep track of the longest palidrome

        while l < len(s) - 1:
            r = len(s) - 1
            if r - l + 1 < len(pali): # no need to continue if the string left is shorter than the palidrome found
                l += 1
                continue
            while r > l:
                if s[r] != s[l]:
                    r -= 1
                else:
                    s2 = s[l : r + 1]
                    if self.isPalidrome(s2) and len(s2) > len(pali):
                        pali = s2
                    r -= 1
            l += 1
        return pali


    def isPalidrome(self, s:str) -> bool:
        l, r = 0, len(s) - 1
        while r >= len(s) / 2 and r > l:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
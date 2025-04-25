# 567. Permutation in String
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool: 
        if len(s1) > len(s2):
            return False
        
        count = {}
        for s in s1:
            count[s] = 1 + count.get(s, 0)
        
        l = 0
        while l + len(s1) <= len(s2):
            count_copy = count.copy()
            for i in range(l, l + len(s1)):
                if s2[i] not in count_copy or count_copy[s2[i]] == 0:
                    l += 1
                    break
                else:
                    count_copy[s2[i]] -= 1

                if i == l + len(s1) - 1:
                    return True
                
        return False

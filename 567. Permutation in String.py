# 567. Permutation in String
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool: 
    # 2nd attempt 
        if len(s2) < len(s1):
            return False
        
        count_s1 = {}
        for s in s1:
            count_s1[s] = 1 + count_s1.get(s, 0)
        
        for i in range(len(s2) - len(s1) + 1):
            if s2[i] not in count_s1:
                continue
            count_s2 = {}
            for s in s2[i:i + len(s1)]:
                if s not in count_s1:
                    break
                else:
                    count_s2[s] = 1 + count_s2.get(s, 0)
            if count_s2 == count_s1:
                return True
            
        return False

    # 1st attempt
    #     if len(s1) > len(s2):
    #         return False
        
    #     count = {}
    #     for s in s1:
    #         count[s] = 1 + count.get(s, 0)
        
    #     l = 0
    #     while l + len(s1) <= len(s2):
    #         count_copy = count.copy()
    #         for i in range(l, l + len(s1)):
    #             if s2[i] not in count_copy or count_copy[s2[i]] == 0:
    #                 l += 1
    #                 break
    #             else:
    #                 count_copy[s2[i]] -= 1

    #             if i == l + len(s1) - 1:
    #                 return True
                
    #     return False

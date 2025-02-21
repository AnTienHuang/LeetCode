# 1899. Merge Triplets to Form Target Triplet
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        valid = set() # tracking index i to see if target[i] is possible to obtain

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i, n in enumerate(target):
                if t[i] == n:
                    valid.add(i)
        
        return len(valid) == 3

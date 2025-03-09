# 347. Top K Frequent Elements
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1

        return sorted(counts, key=counts.get, reverse=True)[:k]

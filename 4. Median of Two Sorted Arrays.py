# 4. Median of Two Sorted Arrays
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        if not nums1:
            i = len(nums2) // 2
            if len(nums2) % 2:
                return nums2[i]
            return (nums2[i] + nums2[i - 1]) / 2
        total = len(nums1) + len(nums2)
        half = total // 2
        i = len(nums1) // 2

        while True:
            k = half - i - 2 # offset for index (both nums1 and nums2)
            nums1_l = nums1[i] if i >= 0 else float("-infinity")
            nums1_r = nums1[i + 1] if i + 1 < len(nums1) else float("infinity")
            nums2_l = nums2[k] if k >= 0 else float("-infinity")
            nums2_r = nums2[k + 1] if k + 1 < len(nums2) else float("infinity")

            if nums1_l <= nums2_r and nums2_l <= nums1_r:
                if total % 2:
                    return min(nums2_r, nums1_r)
                return (max(nums1_l, nums2_l) + min(nums2_r, nums1_r)) / 2
            elif nums1_l > nums2_r:
                i -= 1
            else:
                i += 1

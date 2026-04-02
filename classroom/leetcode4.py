class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = []
        num.extend(nums1)
        num.extend(nums2)
        num.sort()
        n = len(num)
        if n % 2 == 1:
            return num[n // 2]
        elif n % 2 == 0:
            return (num[n // 2 - 1] + num[n // 2]) / 2

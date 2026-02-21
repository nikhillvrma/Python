class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = []
        num.extend(nums1)
        num.extend(nums2)
        n = len(num)
        if n%2 == 1:
            median = num[n//2]
        elif n%
            median = (num[n//2] + num[n+1//2])/2
        return median
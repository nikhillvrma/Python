class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
    # 1st Approach using Bubble Sort : Using this approach we can find the kth largest element, but it throws TLE
        for i in range(0, len(nums)):
            flag = False
            for j in range(0, len(nums)-1):
                if nums[j+1]>nums[j]:
                    temp = nums[j+1]
                    nums[j+1] = nums[j]
                    nums[j] = temp
                    flag = True
            if flag == False:
                break
        return nums[k-1]
    
    # 2nd Approach using Sort() method this approach is better than the 1st approach and it runs in O(nlogn) time complexity
        arr = []
        nums.sort()
        arr.extend(nums[::-1])
        return arr[k - 1]

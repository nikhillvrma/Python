class Solution(object):
    def majorityElement(self, nums):
        
        # method 1:
        for i in range(len(nums)):
            if nums.count(nums[i]) > len(nums) // 2:
                return nums[i]
        
        # method 2
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        ans = 0
        for key in dic:
            if dic[key] >= len(nums)//2:
                return key
                
            
            

nums = [2 , 2, 1, 1, 1, 2, 2]
obj = Solution()
s = obj.majorityElement(nums)
print(s)
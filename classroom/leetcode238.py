def prefixSuffix(nums):
    s = 1
    ans = [1] * len(nums)
    for i in range(1, len(nums)):
        ans[i] = nums[i-1]*ans[i-1]
    for j in range(len(nums)-2, -1, -1):
        s *= nums[j+1]
        ans[j] *= s
    return ans

# nums = [-1, 1, 0, -3, 3]
nums = [1, 2, 3, 4]
r = prefixSuffix(nums)
print(r)

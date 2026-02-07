def productArray(nums):

    ans = []
    for i in range(len(nums)):
        result = 1
        for j in range(len(nums)):
            if nums[j] == nums[i]:
                continue
            result *= nums[j]
        ans.append(result)
    return ans

# nums = [1, 2, 3, 4]
nums = [-1, 1, 0, -3, 3]
r = productArray(nums)
print(r)

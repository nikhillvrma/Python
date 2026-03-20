class Solution:
    def isPalindrome(x):
        n = x
        result = 0
        while n > 0:
            rem = n % 10
            result = (result * 10) + rem
            n = n // 10
        if result == x:
            return True
        else:
            return False

x = int(input("Enter a Number: "))
obj = Solution()
r = obj.isPalindrome(x)
print(r)
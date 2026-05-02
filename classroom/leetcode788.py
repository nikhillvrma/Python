class Solution:
    def rotatedDigits(self, n: int) -> int:
        count = 0
        for i in range(1, n+1):
            num = i
            change = False
            valid = True
            while num>0:
                digit = num % 10
                if digit == 3 or digit == 4 or digit == 7:
                    valid = False
                    break
                if digit == 2 or digit == 5 or digit == 6 or digit == 9:
                    change = True
                num //= 10
            if change and valid:
                count += 1
        return count

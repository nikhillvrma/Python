class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = []

        for row in grid:
            for num in row:
                arr.append(num)

        remainder = arr[0] % x
        for num in arr:
            if num % x != remainder:
                return -1

        arr.sort()
        median = arr[len(arr) // 2]

        ops = 0
        for num in arr:
            ops += abs(num - median) // x

        return ops

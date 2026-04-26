class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Method 1: Max Heap
        maxheap = []
        for x, y in points:
            dist = -(x*x + y*y)
            heapq.heappush(maxheap, (dist, x, y))
            if len(maxheap)>k:
                heapq.heappop(maxheap)
        return [[x, y] for (_, x, y) in maxheap]

        # Method 2: Min Heap
        minheap = []
        for x, y in points:
            distance = (x**2+y**2)
            heapq.heappush(minheap, ([distance, x, y]))
        heapq.heapify(minheap)
        res = []
        while k > 0:
            distance, x, y = heapq.heappop(minheap)
            heapq.heappush(res, [x, y])
            k -= 1
        return res
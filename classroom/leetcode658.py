class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for i in range(len(arr)):
            heapq.heappush(heap, (-1 * abs(arr[i] - x), -arr[i]))
            if len(heap) > k:
                heapq.heappop(heap)
        # heapq.heapify(heap)
        result = []
        while heap:
            result.append(-heapq.heappop(heap)[1])
        return sorted(result)

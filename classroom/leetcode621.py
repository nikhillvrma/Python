class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        freq = [0]*26
        for task in tasks:
            freq[ord(task) - ord('A')]+=1
        heap = []
        for i in range(26):
            if freq[i]!=0:
                heap.append((-1 * freq[i], chr(ord('A')+i)))
        heapq.heapify(heap)
        ans = 0
        while len(heap):
            temp = []
            i = 1
            while i<=n+1:
                if len(heap)>0:
                    t = heapq.heappop(heap)
                    if t[0]+1<0:
                        temp.append([t[0]+1, t[1]])
                    i+=1
                else:
                    break
            if len(temp) == 0 and len(heap) == 0:
                ans += i-1
            else:
                ans += n+1
            for i in temp:
                heapq.heappush(heap, (i[0], i[1]))
        return ans

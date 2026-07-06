class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.maxHeap = []
        heapq.heapify(self.maxHeap)
        for i in stones:
            heapq.heappush(self.maxHeap, i * -1)
        
        while self.maxHeap:
            if len(self.maxHeap) > 1:
                first = heapq.heappop(self.maxHeap)
                second = heapq.heappop(self.maxHeap)
                if first < second:
                    diff = first - second
                    heapq.heappush(self.maxHeap, diff)
            else:
                return self.maxHeap[0] * -1
        return 0
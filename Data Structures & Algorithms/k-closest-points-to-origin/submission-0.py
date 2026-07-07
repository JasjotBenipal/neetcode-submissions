class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])

        heapq.heapify(minHeap)

        res = []

        while k > 0:
            curr = heapq.heappop(minHeap)
            res.append([curr[1], curr[2]])
            k -= 1
        return res
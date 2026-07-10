class MedianFinder:

    def __init__(self):
        self.minstream = []
        self.maxstream = []

    def addNum(self, num: int) -> None:
        if self.minstream and self.maxstream:
            if self.minstream[0] <= num:
                heapq.heappush(self.minstream, num)
            else:
                heapq.heappush(self.maxstream, -num)
        else:
            heapq.heappush(self.minstream, num)
        
        if abs(len(self.minstream) - len(self.maxstream)) > 1:
            if len(self.minstream) > len(self.maxstream):
                heapq.heappush(self.maxstream, -heapq.heappop(self.minstream))
            else:
                heapq.heappush(self.minstream, -heapq.heappop(self.maxstream))

    def findMedian(self) -> float:
        length1 = len(self.minstream)
        length2 = len(self.maxstream)
        
        if ((length1 + length2) % 2) != 0:
            if length1 > length2:
                return float(self.minstream[0])
            else:
                return float(-self.maxstream[0])
        else:
            return (self.minstream[0] + (-self.maxstream[0])) / 2
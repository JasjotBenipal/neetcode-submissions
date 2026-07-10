class MedianFinder:

    def __init__(self):
        self.stream = []

    def addNum(self, num: int) -> None:
        self.stream.append(num)
        self.stream.sort()

    def findMedian(self) -> float:
        length = len(self.stream)
        
        if length % 2 != 0:
            index = length // 2
            return float(self.stream[index])
        else:
            index1 = length // 2
            index2 = index1 - 1
            return (self.stream[index1] + self.stream[index2]) / 2
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cycle = 0

        store = {}
        for i in tasks:
            if i not in store:
                store[i] = 1
            else:
                store[i] += 1
        
        maxHeap = []

        for j in store:
            heapq.heappush(maxHeap, [-store[j], j])
        
        waitlist = []
        stop = 8
        while (maxHeap or waitlist):
            if maxHeap:
                curr = heapq.heappop(maxHeap)
            else:
                curr = None
            cycle += 1
            if curr and curr[0] < -1:
                waitlist.append([curr[1], cycle])
            if waitlist and cycle - waitlist[0][1] >= n:
                if waitlist[0][0] != "None":
                    store[waitlist[0][0]] -= 1
                    if store[waitlist[0][0]] > 0:
                        heapq.heappush(maxHeap, [-store[waitlist[0][0]], waitlist[0][0]])
                del waitlist[0]
            if stop > 0:
                print(cycle)
                print(maxHeap)
                print(waitlist)
                stop -= 1
        return cycle


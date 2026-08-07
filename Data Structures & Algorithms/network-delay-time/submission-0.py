class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visit = set()
        edges = defaultdict(list)

        for u, v, weight in times:
            edges[u].append([v, weight])

        minHeap = [[0, k]]
        time = 0

        while minHeap:
            ptime, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            
            visit.add(node)
            time = max(time, ptime)

            for neigh, neiwei in edges[node]:
                if neigh not in visit:
                    heapq.heappush(minHeap, [ptime + neiwei, neigh])
        
        return time if len(visit) == n else -1
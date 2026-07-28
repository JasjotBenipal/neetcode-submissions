class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        npmap = defaultdict(list)
        for node, pair in edges:
            npmap[node].append(pair)
            npmap[pair].append(node)
        
        visit = set()
        count = 0

        def dfs(node, parent):
            if node in visit:
                return

            visit.add(node)

            for pair in npmap[node]:
                if pair != parent:
                    dfs(pair, node)
            return    

        for node in range(n):
            if node not in visit:
                dfs(node, node - 1)
                count += 1
        
        return count
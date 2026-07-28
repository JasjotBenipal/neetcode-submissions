class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        npmap = defaultdict(list)
        for node, pair in edges:
            npmap[node].append(pair)
            npmap[pair].append(node)
        
        visit = set()

        def dfs(node, parent):
            if node in visit:
                return False
            
            visit.add(node)

            for pair in npmap[node]:
                if pair != parent and not dfs(pair, node):
                    return False
            
            return True
            
        for node in range(n):
            if len(visit) < n and not dfs(node, node - 1):
                return False
        return True
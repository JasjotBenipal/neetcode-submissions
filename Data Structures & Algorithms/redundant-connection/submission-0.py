class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        npmap = defaultdict(list)

        def dfs(node, parent):
            if node in visit:
                return False

            visit.add(node)

            for pair in npmap[node]:
                if pair != parent and not dfs(pair, node):
                    return False
            
            return True


        for node, pair in edges:
            npmap[node].append(pair)
            npmap[pair].append(node)

            visit = set()

            for nodes in npmap:
                if nodes not in visit and not dfs(nodes, 0):
                    return [node, pair]

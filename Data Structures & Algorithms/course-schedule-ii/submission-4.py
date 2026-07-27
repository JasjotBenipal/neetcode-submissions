class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        cpmap = defaultdict(list)
        for crs, preq in prerequisites:
            cpmap[crs].append(preq)
        
        visit = set()
        res = []

        def dfs(crs):
            if crs in visit:
                return []

            if crs in res:
                return 

            if cpmap[crs] == []:
                return res.append(crs)
            
            visit.add(crs)
            
            for preq in cpmap[crs]:
                if dfs(preq) == []:
                    return []
            
            visit.remove(crs)
            cpmap[crs] = []
            return res.append(crs)
        
        
        for crs in range(numCourses):
            if dfs(crs) == []:
                return []
        return res
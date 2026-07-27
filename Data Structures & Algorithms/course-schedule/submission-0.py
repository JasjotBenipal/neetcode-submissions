class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)

        for crs, preq in prerequisites:
            preMap[crs].append(preq)

        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            
            if preMap[crs] == []:
                return True
            
            visit.add(crs)
            for preq in preMap[crs]:
                if not dfs(preq):
                    return False
            
            visit.remove(crs)
            preMap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
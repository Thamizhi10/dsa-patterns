class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=defaultdict(list)
        for src,dest in prerequisites:
            graph[src].append(dest)
            graph[dest]
        visit=set()
        def dfs(course):
            if course in visit:
                return False
            if graph[course]==[]:
                return True
            visit.add(course)
            for i in graph[course]:
                if not dfs(i):
                    return False
            visit.remove(course)
            graph[course]=[]
            return True
        for key in graph:
            if not dfs(key):
                return False
        return True


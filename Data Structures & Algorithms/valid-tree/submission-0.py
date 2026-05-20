class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)>n-1:
            return False
        graph={i:[] for i in range(n)}
        for src,dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)
        visit=set()
        def dfs(node,parent):
            if node in visit:
                return False
            visit.add(node)
            for i in graph[node]:
                if i==parent:
                    continue
                if not dfs(i,node):
                    return False
            return True
        return dfs(0,-1) and len(visit)==n

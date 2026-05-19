class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        dir=[[1,0],[-1,0],[0,1],[0,-1]]
        row,col=len(heights),len(heights[0])
        pac,atl=set(),set()
        def dfs(r,c,s,prevh):
            if (r<0 or c<0 or r>=row or c>=col or heights[r][c]<prevh or (r,c)in s):
                return
            s.add((r,c))
            for dr,dc in dir:
                dfs(r+dr,c+dc,s,heights[r][c])
        for c in range(col):
            dfs(0,c,pac,heights[0][c])
            dfs(row-1,c,atl,heights[row-1][c])
        for r in range(row):
            dfs(r,0,pac,heights[r][0])
            dfs(r,col-1,atl,heights[r][col-1])
        result=[]
        for r in range(row):
            for c in range(col):
                if (r,c) in pac and (r,c) in atl:
                    result.append([r,c])
        return result
            

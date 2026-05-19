class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        row,col=len(grid),len(grid[0])
        islands=0
        def dfs(r,c):
            if(r<0 or r>=row or c<0 or c>=col or grid[r][c]=="0"): # base or pruning condition
                return
            grid[r][c]="0" #making choice
            for dr,dc in directions: #exploring choice
                dfs(r+dr,c+dc)
        for r in range(row):
            for c in range(col):
                if grid[r][c]=="1":
                    islands+=1
                    dfs(r,c)
                    #islands+=1
        return islands
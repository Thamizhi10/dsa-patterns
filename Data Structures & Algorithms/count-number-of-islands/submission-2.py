class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dir=[[1,0],[-1,0],[0,1],[0,-1]]
        row,col=len(grid),len(grid[0])
        islands=0
        def bfs(r,c):
            q=deque()
            q.append((r,c))
            grid[r][c]='0'

            while q:
                ro,co=q.popleft()
                for dr,dc in dir:
                    nr,nc=ro+dr,co+dc
                    if(nr<0 or nc<0 or nr>=row or nc>=col or grid[nr][nc]=='0'):
                        continue
                    q.append((nr,nc))
                    grid[nr][nc]='0'

        for r in range(row):
            for c in range(col):
                if grid[r][c]=='1':
                    bfs(r,c)
                    islands+=1
        return islands
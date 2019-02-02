# class Solution:
#     def numIslands(self, grid):
#         #dfs
#         result = 0
#         for x in range(len(grid)):
#             for y in range(len(grid[0])):
#                 if grid[x][y] == '1':
#                     self.dfs(grid,x,y)
#                     result += 1
#         return result
#     def dfs(self,grid,x,y):
#         direction = [(-1,0),(1,0),(0,-1),(0,1)]
#         grid[x][y] = '0'
#         for dirs in direction:
#             nx = x + dirs[0]
#             ny = y + dirs[1]
#             if 0<=nx<=len(grid)-1 and 0<=ny<=len(grid[0])-1:
#                 if grid[nx][ny] == '1':
#                     self.dfs(grid,nx,ny)

class Solution:
    #bfs
    def numIslands(self,grid):
        result = 0
        que = []
        direction = [(-1,0),(1,0),(0,-1),(0,1)]
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '1':
                    result += 1
                    grid[x][y] = '0'
                    que.append((x,y))
                    while que:
                        i,j = que.pop(0)
                        for dirs in direction:
                            ni,nj = i+dirs[0],j+dirs[1]
                            if 0<=ni<=len(grid)-1 and 0<=nj<=len(grid[0])-1 and grid[ni][nj] == '1':
                                grid[ni][nj] = '0'
                                que.append((ni,nj))
        return result
        
        
        """
        :type grid: List[List[str]]
        :rtype: int
        """

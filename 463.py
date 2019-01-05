class Solution(object):
    def islandPerimeter(self, grid):
        for i in range(len(grid)):
            grid[i].insert(0,0)
            grid[i].append(0)
        grid.insert(0, [0] * (len(grid[0])))
        # grid.insert(-1, [0] * (len(grid[0])))
        grid.append([0] * (len(grid[0])))
        # print(grid)
        result = 0
        base = 0
            
        
        for i in range(1,len(grid)-1):
            for j in range(1,len(grid[0])-1):
                # print(i,j)
                
                if grid[i][j] == 1:
                    base = 4
                    if grid[i][j+1] == 1:
                        base -= 1
                    if grid[i][j-1] == 1:
                        base -= 1
                    if grid[i+1][j] == 1:
                        base -= 1
                    if grid[i-1][j] == 1:
                        base -= 1
                else:
                    base = 0
                # print base
                result = result + base
        return result
                
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
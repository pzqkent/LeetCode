class Solution:
    def isValidSudoku(self, board):
        seen = sum(([(c, i), (j, c), (i//3, j//3, c)]
                    for i, row in enumerate(board)
                    for j, c in enumerate(row)
                    if c != '.'), [])
        print(list([(c, i), (j, c), (i//3, j//3, c)]
                    for i, row in enumerate(board)
                    for j, c in enumerate(row)
                    if c != '.'))
        print(seen)
        return len(seen) == len(set(seen))
    
    # def isValidSudoku(self, board):
    #     seen=[x for i, row in enumerate(board) 
    #                 for j, c in enumerate(row) 
    #                     if c!='.' 
    #                         for x in ((c,i),(j,c),(i//3,j//3,c))]
    #     print(seen)
    #     return len(seen)==len(set(seen))
    
    # def isValidSudoku(self, board):
    #     return 1 == max(collections.Counter(
    #         x
    #         for i, row in enumerate(board)
    #         for j, c in enumerate(row)
    #         if c != '.'
    #         for x in ((c, i), (j, c), (i//3, j//3, c))
    #     ).values() + [1])
    
    
    # def isValidSudoku(self, board):
    #     seen = set()
    #     return not any(x in seen or seen.add(x)
    #                    for i, row in enumerate(board)
    #                    for j, c in enumerate(row)
    #                    if c != '.'
    #                    for x in ((c, i), (j, c), (i//3, j//3, c)))
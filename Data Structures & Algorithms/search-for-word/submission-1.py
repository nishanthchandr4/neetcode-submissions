class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(xIndex, yIndex, i):
            if i == len(word):
                return True
            
            if  not (0 <= xIndex < len(board) and 0 <= yIndex < len(board[0])) or word[i] != board[xIndex][yIndex]:
                return False
            

            tmp = board[xIndex][yIndex]
            board[xIndex][yIndex] = '#'
            res = dfs(xIndex + 1, yIndex, i + 1) or dfs(xIndex - 1, yIndex, i + 1) or dfs(xIndex, yIndex + 1, i + 1) or dfs(xIndex, yIndex - 1, i + 1)
            board[xIndex][yIndex] = tmp
            return res

        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0):
                    return True
        return False

            

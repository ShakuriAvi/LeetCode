from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        return self.__check_matrix(board) and self.__check_cols(board) and self.__check_rows(board)
    def __check_rows(self, board: List[List[str]]) -> bool:
        X, Y = 9,9
        for i in range(X):
            nums = set()
            for j in range(Y):
                if board[j][i] != "." and board[i][j] in nums:
                    return False
                nums.add(board[i][j])

        return True
    def __check_cols(self, board: List[List[str]]) -> bool:
        X, Y = 9,9
        for i in range(X):
            nums = set()
            for j in range(Y):
                if board[j][i] != "." and board[j][i] in nums:
                    return False
                nums.add(board[j][i])

        return True

    def __check_matrix(self, board: List[List[str]]) -> bool:
        X, Y = 3,3
        for i in range(0,X*Y,X):
            for j in range(0, X * Y + 1, X):
                nums = set()

                for k in range(j, j+X):
                    for t in range(i, i+X):
                        if board[k][t] != "." and board[k][t] in nums:
                            return False
                        nums.add(board[k][t])
        return True
if __name__ == '__main__':
    print(Solution().isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))
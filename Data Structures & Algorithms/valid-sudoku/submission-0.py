class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column = defaultdict(set)
        row = defaultdict(set)
        squares = defaultdict(set)

        for outer_loop_row in range(len(board)):
            for inner_loop_column in range(len(board[0])):
                if board[outer_loop_row][inner_loop_column] == ".":
                    continue
                elif ( board[outer_loop_row][inner_loop_column] in row[outer_loop_row]
                    or board[outer_loop_row][inner_loop_column] in column[inner_loop_column]
                    or board[outer_loop_row][inner_loop_column] in squares[(outer_loop_row // 3, inner_loop_column //3)]):
                    return False
                else:
                    column[inner_loop_column].add(board[outer_loop_row][inner_loop_column])
                    row[outer_loop_row].add(board[outer_loop_row][inner_loop_column])
                    squares[(outer_loop_row // 3, inner_loop_column //3)].add(board[outer_loop_row][inner_loop_column])
        return True
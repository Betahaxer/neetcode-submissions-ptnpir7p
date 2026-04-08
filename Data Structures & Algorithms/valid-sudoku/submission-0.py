class Solution: 
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def _get_box(i, j):
            return (i//3) * 3 + j//3
        rows = {i: set() for i in range(9)}
        cols = {i: set() for i in range(9)}
        boxes = {i: set() for i in range(9)}
        for i in range(len(board)):
            for j in range(len(rows)):
                num = board[i][j]
                box = _get_box(i, j)
                if num != ".":
                    if num in rows[i] or num in cols[j] or num in boxes[box]:
                        return False
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[box].add(num)
        return True
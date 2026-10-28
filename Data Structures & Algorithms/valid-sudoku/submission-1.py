class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for num in row:
                if num == ".":
                    continue
                if num in seen:
                    return False
                seen.add(num)
        for col in range(9):
            seen = set()
            for row in range(9):
                num = board[row][col]
                if num == ".":
                    continue
                if num in seen:
                    return False
                seen.add(num)
        # seen = set()
        for startRow in range(0,9,3):
            for startCol in range(0,9,3):
                seen= set()
                for row in range(startRow, startRow +3):
                    for col in range(startCol, startCol +3):
                        num = board[row][col]
                        if num in seen:
                            return False
                        if num == ".":
                            continue
                        seen.add(num)
        return True

                

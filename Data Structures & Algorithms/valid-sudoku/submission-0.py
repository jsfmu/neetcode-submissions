class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set) # Using a defaultdict(set) because we are working with a fixed array
        rows = defaultdict(set)
        squares = defaultdict(set) # key = (r//3, c//3)

        for r in range(9):
            for c in range(9):
                current_num = board[r][c]
                if current_num == ".":
                    continue
                if current_num in rows[r] or current_num in cols[c] or current_num in squares[(r//3, c//3)]:
                    return False
                
                cols[c].add(current_num)
                rows[r].add(current_num)
                squares[(r//3, c//3)].add(current_num)

        return True
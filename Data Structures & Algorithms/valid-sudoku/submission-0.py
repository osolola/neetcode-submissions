class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_seen = [set() for _ in range(9)]
        column_seen = [set() for _ in range(9)]
        result = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[0])):
                cell = board[i][j]
                if cell == ".":
                    continue
                if cell in row_seen[i]:
                    return False
                row_seen[i].add(cell)
                if cell in column_seen[j]:
                    return False
                column_seen[j].add(cell)

                box_key = (i // 3, j // 3)

                if cell in result[box_key]:
                    return False
                
                result[box_key].add(cell)

              
        return True


        
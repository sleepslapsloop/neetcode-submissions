class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #check row
        for row in board:
            counter = Counter(row)
            for key, val in counter.items():
                if key == ".":
                    continue
                if val > 1:
                    return False

        #check col
        for i in range(9):
            hashmap = defaultdict(int)
            for row in board:
                hashmap[row[i]] += 1
                if hashmap[row[i]] > 1 and row[i] != ".":
                    return False

        #check 3x3 grid
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                hashmap = defaultdict(int)
                for i in range(3):
                    for j in range(3):
                        hashmap[board[row + i][col + j]] += 1
                        if hashmap[board[row + i][col + j]] > 1 and board[row + i][col + j] != ".":
                            return False

        return True
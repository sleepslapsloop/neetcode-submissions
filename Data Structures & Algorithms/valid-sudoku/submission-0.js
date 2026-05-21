class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board) {
        let rows = board.length;
        let cols = board[0].length;
        let rowHash =  Array.from(
            { length: rows }, 
            () => new Map()
        );
        for (let i = 0; i < rows; i++) {
            for (let j = 0; j < cols; j++) {
                rowHash[i].set(
                    board[i][j], 
                    (rowHash[i].get(board[i][j]) || 0) + 1
                );
            }
        }

        let colHash = Array.from(
            { length: cols },
            () => new Map()
        );
        for (let i = 0; i < cols; i++) {
            for (let j = 0; j < rows; j++) {
                colHash[i].set(
                    board[j][i], 
                    (colHash[i].get(board[j][i]) || 0) + 1
                );
            }
        }

        let boxHash = Array.from(
            { length: 3 },
            () => Array.from(
                { length: 3 },
                () => new Map()
            )
        );
        for (let i = 0; i < rows; i++) {
            for (let j = 0; j < cols; j++) {
                let sqI = Math.floor(i / 3);
                let sqJ = Math.floor(j / 3);
                boxHash[sqI][sqJ].set(
                    board[i][j],
                    (boxHash[sqI][sqJ].get(board[i][j]) || 0) + 1
                );
            }
        }

        for (let map of rowHash) {
            for (let [key, val] of map) {
                if (key === ".") continue;
                if (val > 1) return false;
            }
        }

        for (let map of colHash) {
            for (let [key, val] of map) {
                if (key === ".") continue;
                if (val > 1) return false;
            }
        }

        for (let row of boxHash) {
            for (let map of row) {
                for (let [key, val] of map) {
                    if (key === ".") continue;
                    if (val > 1) return false;
                }
            }
        }

        return true;
    }
}

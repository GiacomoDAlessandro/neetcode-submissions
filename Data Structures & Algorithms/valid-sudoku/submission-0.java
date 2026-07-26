class Solution {
    public boolean isValidSudoku(char[][] board) {

        Map<Integer, Set<Character>> column = new HashMap<>();
        Map<Integer, Set<Character>> rows = new HashMap<>();
        Map<String, Set<Character>> square = new HashMap<>();

        for (int i = 0; i < board.length; i++) {
            for (int k = 0; k < board[i].length; k++) {
                if (board[i][k] == '.') {continue;}

                String squareKey = (i/3) + "," + (k/3);

                if (rows.computeIfAbsent(i, j -> new HashSet<>()).contains(board[i][k]) ||
                column.computeIfAbsent(k, j -> new HashSet<>()).contains(board[i][k]) ||
                square.computeIfAbsent(squareKey, j -> new HashSet<>()).contains(board[i][k])) {
                    return false;
                }

                rows.get(i).add(board[i][k]);
                column.get(k).add(board[i][k]);
                square.get(squareKey).add(board[i][k]);
            }
        }

        return true;
    }
}

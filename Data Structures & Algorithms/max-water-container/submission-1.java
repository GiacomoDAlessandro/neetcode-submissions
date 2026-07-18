class Solution {
    public int maxArea(int[] heights) {
        int max = 0;

        for (int i = 0; i < heights.length; i++) {
            int first = heights[i];
            for (int j = i; j < heights.length; j++) {
                int used = Math.min(first, heights[j]);
                int sum = (j - i) * (used);
                if (sum > max) {
                    max = sum;
                }
            }
        }

        return max;
    }
}

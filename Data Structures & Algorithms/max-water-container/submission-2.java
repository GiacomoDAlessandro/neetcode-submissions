class Solution {
    public int maxArea(int[] heights) {
        int max = 0;

        int left = 0;
        int right = heights.length - 1;
        for (int i = 0; i < heights.length; i++) {
            if (((right - left) * Math.min(heights[left], heights[right])) > max) {
                max = (right - left) * Math.min(heights[left], heights[right]);
            }
            if (heights[left] < heights[right]) {
                left++;
            } else {
                right--;
            }
            
        }

        return max;
    }
}

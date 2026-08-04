class Solution {
    public int findMin(int[] nums) {
        int min = 0;
        for (int i = 0; i < nums.length; i++) {
            if (i == 0) {
                min = nums[i];
            } else {
                if (min > nums[i]) {
                    min = nums[i];
                }
            }
        }

        return min;
    }
}

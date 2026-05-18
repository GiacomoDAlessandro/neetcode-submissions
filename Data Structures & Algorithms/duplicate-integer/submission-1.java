class Solution {
    public boolean hasDuplicate(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            int number = nums[i];
            for (int k = i + 1; k < nums.length; k++) {
                if (nums[k] == number) {
                    return true;
                }
            }
        }
        return false;
    }
}
class Solution {
    public boolean hasDuplicate(int[] nums) {
        Arrays.sort(nums);
                int k = 1;
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] == nums[k]) {
                return true;
            }
            k++;
        }
        return false;
    }
}
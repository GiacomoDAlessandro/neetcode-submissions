class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> newSet = new HashSet<>();

        for (int i = 0; i < nums.length; i++) {
            if (newSet.contains(nums[i])) {
                return true;
            } else {
                newSet.add(nums[i]);
            }
        }


        return false;
    }
}
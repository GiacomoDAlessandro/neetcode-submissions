class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();
    
        for (int num: nums) {
            set.add(num);
        }
        int longest = 0;
        int curr = 0;
        for (int i = 0; i < nums.length; i++) {
            if (!set.contains(nums[i] - 1)) {
                curr = 1;
                int newNum = nums[i];
                while (set.contains(newNum + 1)) {
                    curr += 1;
                    newNum += 1;
                }
            }
            if (curr > longest) {
                longest = curr;
                 }
        
        }

        return longest;
        
    }
}

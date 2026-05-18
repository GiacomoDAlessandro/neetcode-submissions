class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] answer = new int[2];
        Map<Integer, Integer> map = new HashMap();

        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], i);    
        }

        for (int i = 0; i < nums.length; i++) {
            int difference = target - nums[i];
            
            if (map.containsKey(difference) && map.get(difference) != i) {
                if (map.get(difference) > i) {
                    answer[0] = i;
                    answer[1] = map.get(difference);
                    return answer;
                } else {
                    answer[0] = map.get(difference);
                    answer[1] = i;
                    return answer;
                }
            }
        }
        return answer;
    }
}

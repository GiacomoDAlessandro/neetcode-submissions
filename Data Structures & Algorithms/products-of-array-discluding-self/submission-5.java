class Solution {
    public int[] productExceptSelf(int[] nums) {
        //Answer Array
        int[] answer = new int[nums.length];
        int product = 1;
        int non_zero = 1;
        int zero_counter = 0;
        boolean contains_zero = false;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                non_zero = non_zero * nums[i];
            }
            product = product * nums[i];
            if (nums[i] == 0) {
                zero_counter += 1;
                contains_zero = true;
            }
        }

        if (!contains_zero) {
            for (int i = 0; i < nums.length; i++) {
                answer[i] = product / nums[i];
            }
        } else {
            for (int i = 0; i < nums.length; i++) {
                if (nums[i] != 0) {
                    answer[i] = 0;
                } else {
                    if (zero_counter > 1) {
                        answer[i] = 0;
                    } else {answer[i] = non_zero;}
                }
            }
        }

        return answer;
    }
}  

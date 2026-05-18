class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] answer = new int[nums.length];
        int[] pre = new int[nums.length];
        int[] post = new int[nums.length];

        for (int i = 0; i < nums.length; i++) {
            if (i - 1 >= 0) {
                pre[i] = pre[i - 1] * nums[i];
            } else {
                pre[i] = nums[i];
            }
        }

        for (int i = nums.length - 1; i >= 0; i--) {
            if (i + 1 < nums.length) {
                post[i] = post[i + 1] * nums[i];
            } else {
                post[i] = nums[i];
            }
        }
        for (int i = 0; i < nums.length; i++) {
            System.out.println("pre:" + pre[i]);
            System.out.println("post:" + post[i]);
            if ((i - 1) < 0) {
                answer[i] = post[i + 1];
            } else {
                if ((i + 1) >= nums.length) {
                    answer[i] = pre[i - 1];
                } else {
                    answer[i] = pre[i - 1] * post[i + 1];
                }
            }
        }




        return answer;
    }
}  

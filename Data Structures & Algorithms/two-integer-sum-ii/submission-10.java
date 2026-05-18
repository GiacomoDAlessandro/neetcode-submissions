class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int slow = 0; 
        //Is fine since sum will never be 0 since can't be 0 + 0
        int fast = numbers.length - 1;
        while (numbers[slow] + numbers[fast] != target) {
            if ((numbers[slow] + numbers[fast]) < target) {
                slow++;
            } else {
                fast--;
            }
        }

        return new int[]{slow + 1, fast + 1};
    }
}

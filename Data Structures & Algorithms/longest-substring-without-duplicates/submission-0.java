class Solution {
    public int lengthOfLongestSubstring(String s) {
        int left = 0;
        Set<Character> set = new HashSet<>();
        int max = 0;
        for (int i = 0; i < s.length(); i++) {
            while (set.contains(s.charAt(i))) {
                set.remove(s.charAt(left));
                left += 1;
            }
            set.add(s.charAt(i));
            max = Math.max(max, i - left + 1);
        }


        return max;
    }
}

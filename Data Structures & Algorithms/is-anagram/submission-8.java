class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        int length = s.length();

        Queue<Character> queueS = new PriorityQueue<>();
        Queue<Character> queueT = new PriorityQueue<>();

        for (int i = 0; i < length; i++) {
            queueS.add(s.charAt(i));
            queueT.add(t.charAt(i));
        }

        for (int i = 0;i < length; i++) {
            if (!queueT.contains(s.charAt(i))) {
                return false;
            }
            queueT.remove(s.charAt(i));
        }

        return true;
    }
}

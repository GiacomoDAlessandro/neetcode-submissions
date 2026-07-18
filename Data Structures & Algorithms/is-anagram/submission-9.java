class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {return false;}

        char[] sArray = new char[s.length()];
        sArray = s.toCharArray();

        char[] tArray = new char[t.length()];
        tArray = t.toCharArray();
        Arrays.sort(tArray);
        Arrays.sort(sArray);
        for (int i = 0; i < s.length(); i++) {
            if (tArray[i] != sArray[i]) {
                return false;
            }
        }

        return true;
    }
}

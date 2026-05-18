class Solution {
    public boolean isPalindrome(String s) {
        String noWhiteSpace = "";
        for (int i = 0; i < s.length(); i++) {
            if (!Character.isWhitespace(s.charAt(i)) && Character.isLetterOrDigit(s.charAt(i))) {
                noWhiteSpace += Character.toLowerCase(s.charAt(i));
            }
        }

        String newString = "";
        for (int i = noWhiteSpace.length() - 1; i >= 0; i--) {
            newString += noWhiteSpace.charAt(i);
        }  

        
        if (noWhiteSpace.equals(newString)) {
            return true;
        } else {
            return false;
        }
    }
}

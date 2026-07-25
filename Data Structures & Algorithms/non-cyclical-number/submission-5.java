class Solution {
    public boolean isHappy(int n) {
        int sum = 0;
        int size = 0;
        Set<Integer> set = new HashSet<>();
        
        if (sum == 1) {
            return true;
        }

        while (n != 1) {
            size = String.valueOf(n).length();
            for (int i = 0; i < size; i++) {
                char firstChar = String.valueOf(Math.abs(n)).charAt(i);
                int firstDigit = Character.getNumericValue(firstChar);
                sum += firstDigit * firstDigit;
            }
            System.out.println("Sum: " + sum);
            n = sum;
            sum = 0;
            if (set.contains(n)) {
                return false;
            } else {
                set.add(n);
            }
        }

        return true;
    }
}

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();


        for (int i = 0; i < strs.length; i++) {
            int[] count = new int[26]; 
            for (int a = 0; a < strs[i].length(); a++) {          
                count[strs[i].charAt(a) - 'a']++;
            }
            String check = Arrays.toString(count);
            if (map.containsKey(check)) {
                map.get(check).add(strs[i]);
            } else {
                List<String> newList = new ArrayList<>();
                newList.add(strs[i]);
                map.put(check, newList);
            }
        }
        return new ArrayList<>(map.values());
    }
}

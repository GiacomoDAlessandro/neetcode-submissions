class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        HashMap<String, List<String>> map = new HashMap<>();


        for (int i = 0; i < strs.length; i++) {
            int[] count = new int[26];
            
            for (int k = 0; k < strs[i].length(); k++) {
                count[strs[i].charAt(k) - 'a'] += 1;
                String key = Arrays.toString(count);
            }
            
            String key = Arrays.toString(count);

            if (map.containsKey(key)) {
                map.get(key).add(strs[i]);
            } else {
                List<String> list = new ArrayList<>();
                list.add(strs[i]);
                map.put(key, list);
            }
        }

      return new ArrayList(map.values());
    }
}

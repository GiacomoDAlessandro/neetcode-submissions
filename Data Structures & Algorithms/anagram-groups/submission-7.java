class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
      HashMap<String, List<String>> map = new HashMap<>();  
      

      for (int i = 0; i < strs.length; i++) {
        char[] sorted = strs[i].toCharArray();
        Arrays.sort(sorted);
        String newString = new String(sorted);
        if (map.containsKey(newString)) {
            map.get(newString).add(strs[i]);
        } else {
            List<String> newList = new ArrayList<>();
            newList.add(strs[i]);
            map.put(newString, newList);
        }
      }

      return new ArrayList(map.values());
    }
}

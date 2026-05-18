class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();


        for (int i = 0; i < strs.length; i++) {
            char[] sortArray = strs[i].toCharArray();
            Arrays.sort(sortArray);
            String word = new String(sortArray);
            List<String> tempList = map.get(word);
            if (tempList == null) {
                tempList = new ArrayList<>();
                tempList.add(strs[i]);
                map.put(word, tempList);
            } else {
                tempList.add(strs[i]);
            }
        }


        return new ArrayList(map.values());
    }
}

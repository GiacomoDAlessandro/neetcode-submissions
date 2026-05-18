class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        List<List<String>> finalList = new ArrayList<>();

        for (int i = 0; i < strs.length; i++) {
            char[] newSort = strs[i].toCharArray();
            Arrays.sort(newSort);
            String word = new String(newSort);
            boolean contains = false;
            for (List<String> newList: finalList) {
                char[] doubleSort = newList.get(0).toCharArray();
                Arrays.sort(doubleSort);
                String newWord = new String(doubleSort);
                if (newWord.equals(word)) {
                    newList.add(strs[i]);
                    contains = true;
                }
            }
            
            if (!contains) {
                List<String> allNew = new ArrayList<>();
                allNew.add(strs[i]);
                finalList.add(allNew);
            } else {
                contains = false;
            }

    }

    return finalList;
    }
}

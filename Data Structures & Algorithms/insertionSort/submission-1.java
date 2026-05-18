// Definition for a pair
// class Pair {
//     int key;
//     String value;
//
//     Pair(int key, String value) {
//         this.key = key;
//         this.value = value;
//     }
// }
public class Solution {
    public List<List<Pair>> insertionSort(List<Pair> pairs) {
        List<List<Pair>> sorted = new ArrayList<>();

        for (int i = 0; i < pairs.size(); i ++) {
            int val = pairs.get(i).key;
            Pair placeholder = pairs.get(i);

            
            for (int j = 0; j < i; j++) {
                if (val < pairs.get(j).key) {
                    pairs.remove(placeholder);
                    pairs.add(j,placeholder);
                    break;
                }
            }
            
            sorted.add(new ArrayList<>(pairs));
        }

return sorted;
    }

}

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int[] answer = new int[k];
        //First is Num, second is counter
        Map<Integer, Integer> map = new HashMap<>();
        PriorityQueue<Integer> heap = new PriorityQueue<>((a, b) -> map.get(a) - map.get(b));
        for (int num: nums) {
            if (map.containsKey(num)) {
                int iterate = map.get(num);
                map.put(num, iterate+1);
            } else {
                map.put(num, 1);
            }
        }

        for (Integer key : map.keySet()) {
            heap.offer(key);
        }
       
       int j =0;
       int size = heap.size();
       for (int i =0; i < size; i++) {
        if (heap.size() > k) {
            heap.poll();
            } else {
                answer[j] = heap.poll();
                j++;
             }
             }
       
        return answer;
        
    }
}

class Solution {

    public String encode(List<String> strs) {
        String encoded = "";
        for (int i = 0; i < strs.size(); i++) {
            encoded += strs.get(i).length() + "?" + strs.get(i);
        }
        System.out.println(encoded);

        return encoded;
    }

    public List<String> decode(String str) {
        List<String> answer = new ArrayList<>();
        int wNum = 0;
        int i = 0;
        while (i < str.length()) {
            
            int j = i;
            while (!(str.charAt(j) == ('?'))) {
                j++;
            }
            wNum = Integer.parseInt(str.substring(i, j));
            String word = str.substring(j + 1, j + 1 + wNum);
            answer.add(word);
            i = j + 1 + wNum;
            }
            return answer;

        }
    }
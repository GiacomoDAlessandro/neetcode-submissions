class Solution {
    public int maxProfit(int[] prices) {
        int min = prices[0];
        int profit = 0;
        for (int right = 0; right < prices.length; right++) {
            if (prices[right] < min) {
                min = prices[right];
            }
            if (prices[right] - min > profit) {
            profit = prices[right] - min;
            }
        }

        return profit;
    }
}

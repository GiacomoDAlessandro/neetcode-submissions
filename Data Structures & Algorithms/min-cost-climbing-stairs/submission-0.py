class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        sum = [0] * len(cost)
        for i, num in enumerate(cost):
            if i == 0:
                sum[i] = min(cost[i], cost[i + 1])
            elif i == len(cost) - 1:
                return sum[i - 1]
            else:
                sum[i] = min(sum[i - 1] + cost[i + 1], sum[i - 2] + cost[i])
            print(sum)
        
        return sum[len(cost) - 1]
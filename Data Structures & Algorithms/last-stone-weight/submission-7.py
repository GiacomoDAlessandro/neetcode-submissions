class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        
        
        while len(stones) > 1:
            print(stones)
            if stones[len(stones)-1] == stones[len(stones) - 2]:
                stones.pop()
                stones.pop()
            else:
                diff = abs(stones[len(stones) - 1] - stones[len(stones) - 2])
                stones.pop()
                stones[len(stones) - 1] = diff
            stones.sort()
        return stones[0] if stones else 0
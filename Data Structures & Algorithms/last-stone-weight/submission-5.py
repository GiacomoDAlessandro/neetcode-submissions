class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:

            stones.sort()

            cur = stones.pop() - stones.pop()
            if cur != 0:
                stones.append(cur)
        
        if not stones:
            return 0
        else:
            return stones[0]
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            mid = (l + r) // 2
            totalSum = 0
            print(l)
            print(r)
            for pile in piles:
                totalSum += math.ceil(pile/mid)
            if totalSum > h:
                l = mid + 1
            elif totalSum <= h:
                r = mid - 1
            else:
                return l
            print(totalSum)
        return l
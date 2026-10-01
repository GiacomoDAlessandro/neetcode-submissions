class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        sor = sorted(d, key=d.get)
        sor = sor[::-1]
        return sor[:k]

        
            
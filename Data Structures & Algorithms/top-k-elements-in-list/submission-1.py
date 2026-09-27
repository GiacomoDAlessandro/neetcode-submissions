class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(list)
        
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        arr = []
        for num, cnt in d.items():
            arr.append([cnt, num])
        res = []
        arr.sort()
        while len(res) < k:
            res.append(arr.pop()[1])
        return res

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        s = set()
        s.add(0)
        t = sum(nums) // 2
        for i in range(len(nums) - 1, -1, -1):
            n = set()
            for j in s:
                n.add(j + nums[i])
                n.add(j)
            s = n

        return True if t in s else False
        

        

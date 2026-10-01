class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        
        l, r = 0, 1
        while r < len(nums):
            print(l, r)
            if nums[l] == nums[r]:
                return True
            r += 1
            l += 1
        return False
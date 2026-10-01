class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        nums.sort()
        l, r = 0, 1
        maxC = 0
        count = 1
        print(nums)
        while r < len(nums):
            
            if nums[l] + 1 == nums[r]:
                count += 1
                l += 1
                r += 1
            elif nums[l] == nums[r]:
                l += 1
                r += 1
            else:
                maxC = max(maxC, count)
                count = 1
                l += 1
                r += 1
            maxC = max(maxC, count)
        return maxC
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = 1
        for i in range(len(nums)):
            nums.append(nums[i])
            n += 1
        return nums

        
        
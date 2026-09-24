class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i, num in enumerate(nums):
            if (target - num) in d:
                print(i)
                return [d[target - num], i]
            d[num] = i
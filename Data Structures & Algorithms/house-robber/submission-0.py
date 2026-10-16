class Solution:
    def rob(self, nums: List[int]) -> int:
        arr = [0] * len(nums)
        
        for i in range(len(arr)):
            if i == 0:
                arr[i] = nums[i]
            elif i == 1:
                arr[i] = max(arr[i - 1], nums[i])
            else:
                arr[i] = max(arr[i - 2] + nums[i], arr[i - 1])
        return arr[-1]
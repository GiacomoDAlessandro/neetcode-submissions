class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i, num in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if num == nums[j]:
                    t = abs(i - j)
                    if t <= k:
                        return True


        return False
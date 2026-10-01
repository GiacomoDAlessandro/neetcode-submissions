class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = math.prod(nums)
        res = [prod] * len(nums)

        for i, num in enumerate(nums):
            if num == 0:
                temp = nums.copy()
                del temp[i]
                res[i] = math.prod(temp)
            else:
                res[i] = res[i] // num
        
        return res
        

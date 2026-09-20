class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        print(nums)
        answer = []
        for i, num in enumerate(nums):
            if (num > 0):
                break
            
            l = i + 1
            r = len(nums) - 1

            while l < r:
                sum = num + nums[l] + nums[r]
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    if not [num, nums[l], nums[r]] in answer:
                        answer.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    
        return answer
        

       
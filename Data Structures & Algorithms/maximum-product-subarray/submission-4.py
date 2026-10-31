class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m = max(nums)
        #Keep track of min and max
        arr = [[0 for __ in range(len(nums))] for __ in range(2)]
        for i, num in enumerate(nums):
            #ignore 0s
            if num == 0:
                arr[0][i] = arr[1][i] = 0
            elif i == 0:
                #max
                arr[0][i] = num
                #min
                arr[1][i] = num
            else:
                arr[0][i] = max(arr[0][i - 1] * num, num, arr[1][i-1] * num)
                arr[1][i] = min(arr[1][i - 1] * num, num, arr[0][i-1] * num)
                
        
        return max(m, max(arr[0]))

        #could look at each one as looking left and right, if i == 0, 
        #check the left since out of bounds check product w/ right, 
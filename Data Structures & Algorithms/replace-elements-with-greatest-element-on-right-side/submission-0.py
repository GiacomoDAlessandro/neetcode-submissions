class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        ans = [0] * len(arr)
        currMax = -1
        
        for i in range(len(arr) - 1, -1, -1):
            print(i)
            ans[i] = currMax
            currMax = max(currMax, arr[i])

        return ans
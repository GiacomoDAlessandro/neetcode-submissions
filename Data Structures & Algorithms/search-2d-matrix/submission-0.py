class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        cols, rows = len(matrix), len(matrix[0])
        

        bot, top = 0, cols - 1

        while bot < top:
            res = (bot + top) // 2
            
            if matrix[res][0] == target or matrix[res][rows - 1] == target:
                return True
            elif matrix[res][0] > target:
                top = res - 1
            elif matrix[res][rows - 1] < target:
                bot = res + 1
            else:
                bot, top = res, res
                break

        
        l, r = 0, rows - 1
        print(bot, top)
        while l <= r:
            mid = (l + r) // 2
            if matrix[bot][mid] == target:
                return True
            elif matrix[bot][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
            
        return False
            
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return [1]
        size = len(digits) - 1
        if digits[size] != 9:
            digits[size] += 1
            return digits
        else:
            digits[size] = 0
            return self.plusOne(digits[:-1]) + [0]
            
        
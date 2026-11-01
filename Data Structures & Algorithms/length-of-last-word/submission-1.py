class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        print(s)
        s = s.strip()
        
        arr = s.split(' ')
        print(s, arr)
        return len(arr[len(arr) - 1])
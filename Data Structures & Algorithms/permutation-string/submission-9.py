class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        a1 = [0] * 26
        
        for i in s1:
            a1[ord(i) - ord('a')] += 1
        

        l, r = 0, len(s1) - 1
        temp = [0] * 26
        for q in range(l, r + 1):
            temp[ord(s2[q]) - ord('a')] += 1
        while r < len(s2):
            if r != len(s1) - 1:
                temp[ord(s2[r]) - ord('a')] += 1
            if a1 == temp:
                return True
            temp[ord(s2[l]) - ord('a')] -= 1
            l += 1
            r += 1
            

        return False
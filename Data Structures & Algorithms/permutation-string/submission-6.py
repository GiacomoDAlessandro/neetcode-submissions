class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a1 = [0] * 26
        
        for i in s1:
            a1[ord(i) - ord('a')] += 1
        

        l, r = 0, len(s1)
        while r <= len(s2):
            temp = [0] * 26
            for x in range(l, r):
                temp[ord(s2[x]) - ord('a')] += 1
            if a1 == temp:
                return True
            l += 1
            r += 1

        

        return False
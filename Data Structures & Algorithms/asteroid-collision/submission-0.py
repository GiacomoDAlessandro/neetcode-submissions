class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        
        for a in asteroids:
            
            while s and a < 0 and s[-1] > 0:
                if abs(a) == s[-1]:
                    s.pop()
                    a = 0
                elif abs(a) > s[-1]:
                    s.pop()
                else:
                    a = 0
            if a != 0:
                s.append(a)
                

        return s
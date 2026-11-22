class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        
        for i in asteroids:
            if not s:
                s.append(i)
            elif s[-1] < 0 and i < 0:
                s.append(i)
            elif s[-1] > 0 and i > 0:
                s.append(i)
            elif s[-1] < 0 and i > 0:
                s.append(i)
            else:
                while s and s[-1] > 0 and i < 0:
                    if s[-1] == abs(i):
                        s.pop()
                        break
                    elif s[-1] < abs(i):
                        s.pop()
                        if not s or s[-1] < 0:
                            s.append(i)
                    else:
                        break
        return s        

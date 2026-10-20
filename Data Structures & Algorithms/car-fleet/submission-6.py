class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars.sort(reverse=True)
        count = 0
        prevSpeed = 0
        for i in cars:
            time = (target - i[0]) / i[1]
            if time > prevSpeed:
                count += 1
                prevSpeed = time
            else:
                continue
        
        return count

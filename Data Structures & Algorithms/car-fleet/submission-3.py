class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = 0
        recFin = 0
        pairs = list(zip(position, speed))
        pairs.sort(key=lambda p:p[0])
        s = []
        for i in pairs:
            s.append(i)

        while s:
            pair = s.pop()
            time = (target - pair[0]) / pair[1]

            if time > recFin:
                fleet += 1
                recFin = time
            else:
                continue
        
        return fleet

        
        
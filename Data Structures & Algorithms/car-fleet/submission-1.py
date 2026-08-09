class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        
        cars.sort(reverse = True)

        result = []

        for pos, spd in cars:
            time = (target - pos) / spd

            if not result:
                result.append(time)
            elif time > result[-1]:
                result.append(time)
            
        return len(result)
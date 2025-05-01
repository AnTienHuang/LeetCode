#853. Car Fleet
class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = [[p, s] for p, s in zip(position, speed)]
        cars.sort(reverse=True)
        times = [(target - p) / s for p, s in cars]
        res = [times[0]]
        for t in times[1:]:
            if t > res[-1]:
                res.append(t)
        
        return len(res)

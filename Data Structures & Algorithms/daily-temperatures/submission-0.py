class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            dt = temperatures[i]

            while stack and dt > temperatures[stack[-1]]:
                prev = stack.pop()
                result[prev] = i - prev
            
            stack.append(i)
        
        return result

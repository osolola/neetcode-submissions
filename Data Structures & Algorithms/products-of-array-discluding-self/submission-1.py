class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            
            number = 1
            if(i == 0):
                number *= 1
            else:
                for k in range(0, i):
                    number *= nums[k]

            for j in range(i + 1, len(nums)):
                number *= nums[j] 
            
            result.append(number)

        return result
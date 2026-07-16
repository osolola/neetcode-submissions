class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_nums = sorted(nums)
        
        for i in range(len(nums) - 1):
            x = new_nums[i]
            y = new_nums[i + 1]

            if(x == y):
                return True

        return False
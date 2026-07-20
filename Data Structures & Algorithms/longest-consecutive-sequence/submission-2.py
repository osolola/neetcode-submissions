class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()

        final_answer = [];
        longest = 0

        for i in range(len(nums)):
            seen.add(nums[i])
        
        for num in seen:
            if (num - 1) not in seen:
                length = 1
                next_num = num + 1

                while next_num in seen:
                    length += 1
                    next_num += 1     
                longest = max(longest, length)

        
        return longest
            
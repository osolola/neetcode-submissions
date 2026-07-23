class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        poop = set()
        left = 0
        result = 0
        for right in range(len(s)):
            while s[right] in poop:
                poop.remove(s[left])
                left += 1
            poop.add(s[right])
            
            result = max(result, right - left + 1)

        return result
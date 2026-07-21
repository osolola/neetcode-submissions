import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        left = 0
        right = len(new_string) - 1

        while left < right:
            if new_string[left] != new_string[right]:
                return False
            
            left += 1
            right -= 1
        
        return True
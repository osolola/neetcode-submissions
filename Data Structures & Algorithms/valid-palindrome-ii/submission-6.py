class Solution:

    def palindrome(self, s, l, r) -> bool:
        while (l < r):
            if (s[l] == s[r]):
                l += 1
                r -= 1
            else:
                return False
        
        return True
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        result = True


        while (left < right):
            if (s[left] == s[right]):
                left += 1
                right -= 1
                continue
            else:
                return self.palindrome(s, left + 1, right) or self.palindrome(s, left, right - 1)
            

        return True
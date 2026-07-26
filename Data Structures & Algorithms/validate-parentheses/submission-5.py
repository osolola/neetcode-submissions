class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opens = "{[("
        pairs = {")" : "(", "}" : "{", "]" : "["}

        for i in range(len(s)):
            if s[i] in opens:
                stack.append(s[i])
            else:
                if not stack or stack.pop() != pairs[s[i]]:  
                    return False
        
        return not stack
        
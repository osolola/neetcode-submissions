class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "/", "*"}
        
        for i in range(len(tokens)):
            if tokens[i] in operators:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                result = 0
                if tokens[i] == "+":
                    result = num1 + num2
                elif tokens[i] == "-":
                    result = num2 - num1
                elif tokens[i] == "*":
                    result = num1 * num2
                elif tokens[i] == "/":
                    
                    result = int(num2 / num1)
                
                stack.append(result)
            else:
                stack.append(int(tokens[i]))
            
        return stack.pop()
                    

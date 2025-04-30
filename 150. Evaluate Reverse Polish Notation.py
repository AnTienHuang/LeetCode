# 150. Evaluate Reverse Polish Notation
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for t in tokens:
            if t not in ["+", "-", "*", "/"]:
                stack.append(int(t))
            else:
                a = stack.pop()
                b = stack.pop()
                match t:
                    case "+":
                        stack.append(a + b)
                    case "-":
                        stack.append(b - a)
                    case "*":
                        stack.append(a * b)
                    case "/":
                        stack.append(int(b / a))
        
        return stack[0]
        
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op_chars = ['+', '-', '*', '/']
        stack = []
        for i in range(len(tokens)):
            if tokens[i] in op_chars:
                second = int(stack.pop())
                first = int(stack.pop())
                match tokens[i]:
                    case "+":
                        stack.append(first + second)
                    case "-":
                         stack.append(first - second)
                    case "*":
                         stack.append(first * second)
                    case "/":
                         stack.append(first / second)
            else: 
                stack.append(tokens[i])
        print(stack)
        return int(stack[0])


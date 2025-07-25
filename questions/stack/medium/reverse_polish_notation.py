class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        for i in range(len(tokens)-1, -1, -1):
            stack.append(tokens[i]);
        
        buffer_arr = []
        op_chars = ['+', '-', '*', '/']
        while not len(stack) == 0:
            print("stack", stack)
            current = stack.pop()
            print("CURRENT", current)
            if current not in op_chars:
                buffer_arr.append(int(current))
                print(buffer_arr)
            else:
                match current:
                    case "+":
                        stack.append(sum(buffer_arr))
                    case "-":
                         stack.append(buffer_arr[0] - buffer_arr[1])
                    case "*":
                         stack.append(buffer_arr[0] * buffer_arr[1])
                    case "/":
                         stack.append(buffer_arr[0] / buffer_arr[1])
                buffer_arr = []
                if len(stack) ==1:
                    break
                        
        return stack[0]


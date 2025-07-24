class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)-1, -1, -1):
            stack.append(tokens[i]);
        

        
        answer = None
        buffer_arr = []
        while len(stack) =! 0:
            current = stack.pop()
            if isinstance(current, int):
                buffer_arr.append(current)
            else:
                match current:
                    case "+":
                        if answer = None:
                            answer = sum(buffer_arr)
                        else:
                            answer += sum(buffer_arr)
                    case "-":
                        remainder = buffer_arr[0]
                        for i in range(1, len(buffer_arr)-1):
                            remainder-= buffar_ar[i]
                        if answer = None:
                            answer = remainder
                        else:
                            answer -= remainder
                    case "*":
                        remainder = buffer_arr[0]
                        for i in range(1, len(buffer_arr)-1):
                            remainder-= buffar_ar[i]
                        if answer = None:
                            answer = remainder
                buffer_sum = []
 

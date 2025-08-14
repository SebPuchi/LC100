class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        if len(temperatures) > 1:
            answer = [0] * len(temperatures)
            stack = []
            for i in range(len(temperatures)):
                while len(stack) > 0 and stack[-1][0] < temperatures[i]:
                    current, index = stack.pop()
                    answer[index] = i - index
                stack.append((temperatures[i],i))
            return(answer)
        else:
            return [0]

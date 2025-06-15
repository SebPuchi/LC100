class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.current_min = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.current_min == None:
            self.current_min = val
            self.min_stack.append(val)
        elif val <= self.current_min:
            self.current_min = val
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack[len(self.stack)-1] == self.current_min:
            self.min_stack.pop()
            if len(self.min_stack) != 0:
                self.current_min = self.min_stack[len(self.min_stack)-1]
            else:
                self.current_min = None
        self.stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        return self.current_min


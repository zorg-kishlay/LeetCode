class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        minno = val
        if len(self.minstack):
            lastNumber = self.minstack[len(self.minstack)-1]
            minno= min(lastNumber, val)
        
        self.stack.append(val)
        self.minstack.append(minno)
        
        

    def pop(self) -> None:
        self.minstack.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        return self.minstack[len(self.minstack)-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        low = val
        if self.stack:
            low = min(low, self.getMin())
        self.stack.append((val,low))
        
    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        value, _low = self.stack[-1]
        return value
        
    def getMin(self) -> int:
        value,low = self.stack[-1]
        return low


        

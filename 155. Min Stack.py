# 155. Min Stack
class MinStack():
    def __init__(self):
        self.stack = []
        self.min_values = []
    
    def push(self, val: int):
        self.stack.append(val)
        if not self.min_values or val <= self.min_values[-1]:
            self.min_values.append(val)
    
    def pop(self):
        if self.stack:
            v = self.stack.pop()
            if v == self.min_values[-1]:
                self.min_values.pop()
    
    def top(self):
        if self.stack:
            return self.stack[-1]
    
    def getMin(self):
        if self.min_values:
            return self.min_values[-1]
        
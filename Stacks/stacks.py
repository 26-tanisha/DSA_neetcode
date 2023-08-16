#implemented uding dynamic array
class stack:
    def __init__(self):
        self.stack = []
    def push(val,self):
        self.stack.append(val)
    def pop(self):
        return self.stack.pop()
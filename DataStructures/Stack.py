class Stack:

    def __init__(self):
        self.size = 0
        self.stack = []

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        del self.stack[len(self.stack)-1]

    def peek(self):
        print(self.stack[len(self.stack)-1])

    def traverse(self):
        print(self.stack[::-1])

if __name__ =="__main__":
    s = Stack()
    s.push(10)
    s.push(40)
    s.push(25)
    s.push(76)
    s.push(23)
    s.traverse()
    s.pop()
    s.traverse()
    s.peek()
    s.push(90)
    s.traverse()
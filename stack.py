class Stack(list):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            raise Exception("Stack is empty")

    def top(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(5)
    stack.push(7)

    print(stack.size())

    print(stack.top())
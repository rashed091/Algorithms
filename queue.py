from collections import deque

class Queue(object):
    def __init__(self):
        self.items = deque()

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft()

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            raise Exception("Stack is empty")


if __name__ == "__main__":
    queue = Queue()

    queue.enqueue(5)
    queue.enqueue(3)
    queue.enqueue(7)

    print(queue.dequeue())
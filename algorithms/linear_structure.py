class Queue:
    def __init__(self):
        self.queue = []

    def put(self, elem):
        self.queue.append(elem)

    def pop(self):
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)


class Stack:
    def __init__(self):
        self.items = []

    def push(self, el):
        self.items.append(el)

    def peek(self):
        return self.items[-1]

    def pop(self):
        return self.items.pop(-1)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

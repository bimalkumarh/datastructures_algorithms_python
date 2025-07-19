class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.items = [None] * size
        self.front = -1
        self.rear = -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def is_empty(self):
        return self.front == -1

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full. Cannot enqueue:", item)
            return

        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.items[self.rear] = item
        print(f"After enqueueing item: {item} queue: {self.items} front: {self.front} rear: {self.rear}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return

        removed = self.items[self.front]
        self.items[self.front] = None

        if self.front == self.rear:
            # Only one element was present
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        print(f"After dequeueing item: {removed} queue: {self.items} front: {self.front} rear: {self.rear}")


obj = CircularQueue(3)
obj.enqueue(4)
obj.enqueue(5)
obj.enqueue(7)
obj.enqueue(8)
obj.dequeue()
obj.dequeue()
obj.dequeue()
obj.enqueue(11)
obj.enqueue(34)
obj.enqueue(5)
obj.enqueue(7)
obj.enqueue(10)
obj.enqueue(33)
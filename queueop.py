class Queue:
    def __init__(self, size):
        self.size = size
        self.items = [None] * size
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return self.rear == self.size - 1

    def enqueue(self, item):
        if self.is_full():
            print(f"Queue is full, cant insert {item}")
            return

        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear += 1

        self.items[self.rear] = item
        print(f"Queue items {item} after enqueue: {self.items} Front: {self.front}, Rear: {self.rear}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return

        removed = self.items[self.front]
        self.items[self.front] = None

        if self.front == self.rear:
            # Only one element left
            self.front = self.rear = -1
        else:
            self.front += 1

        print(f"Queue items after dequeue: {self.items} Front: {self.front}, Rear: {self.rear}")

obj = Queue(3)
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)                        
obj.dequeue()  
obj.dequeue() 
obj.enqueue(8)  
obj.enqueue(9)     

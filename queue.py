class QueueList:
    def __init__(self):
        self.items = []

    def enqueue(self, data):
        return self.items.append(data)

    def dequeue(self):
        if self.is_empty():
            return IndexError("Queue is Empty")
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return IndexError("Queue is Empty")
        return self.items[0]

    def show_queues(self):
        return self.items
    

    def is_empty(self):
        return len(self.items) == 0



q1 = QueueList()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(4)
q1.enqueue(6)
q1.dequeue()
print(q1.show_queues())

















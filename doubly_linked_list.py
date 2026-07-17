class Node:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self,val):
        pass
    def insert_at_tail(self,val):
        pass
    def delete_at_head(self):
        pass
    def delete_at_tail(self):
        pass
    def insert_at_position(self,value,position):
        pass
    def delete_at_position(self,position):
        pass
    def search(self, value):
        pass
    def traverse_forward(self):
        pass
    def traverse_backword(self):
        pass

if __name__ == '__main__':
    l1 = DoublyLinkedList()
class Node:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_at_head(self,val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1
        return
    def insert_at_tail(self,val):
        new_node = Node(val)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.size += 1
        return
        
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
        if self.head is None:
            print("Linked List is Empty")
            return
        itr = self.head
        list1 = ''
        while itr:
            list1 += str(itr.val) + '-->'
            itr = itr.next
        print(list1)
        return
    def traverse_backword(self):
        pass

if __name__ == '__main__':
    l1 = DoublyLinkedList()
    l1.insert_at_head(4)
    l1.insert_at_head(3)
    l1.insert_at_head(2)
    l1.insert_at_tail(5)
    l1.traverse_forward()
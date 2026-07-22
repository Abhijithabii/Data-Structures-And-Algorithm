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
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1
        return
        
    def delete_at_head(self):
        if self.head is None:
            print('Empty Linked List')
            return None
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

        self.size -= 1
        return


    def delete_at_tail(self):
        if self.tail is None:
            print("Linked List is Empty")
            return None
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            prev_last = self.tail.prev
            prev_last.next = None
        self.size -= 1

    def insert_at_position(self,value,position):
        """
        Insert a node at a specific position (0-indexed).
        position = 0 means head, position = size means tail.
        """
        if position < 0 or position > self.size -1:
            print("Index Out of Range")
            return
        new_node = Node(value)
        if position == 0:
            self.insert_at_head(value)
            return
        if position == self.size -1:
            self.insert_at_tail(value)
            return
        
       
        current = self.head

        for _ in range(position):
            current = current.next
        
        new_node.next = current
        new_node.prev = current.prev

        current.prev.next = new_node
        current.prev = new_node
        self.size += 1
        return



        
    def delete_at_position(self,position):
        pass
    def delete_by_value(self,value):
        pass
    def get_size(self):
        return self.size
    def get_head(self):
        return self.head.val if self.head else None
    def get_tail(self):
        return self.tail.val if self.tail else None

    def search(self, value):
        current = self.head
        while current:
            if current.val == value:
                print("The search value present in the linked list")
                return
            current = current.next
        print("The searched value not present in the linked list")
        return

    def traverse_forward(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        itr = self.head
        list1 = ''
        while itr:
            list1 += '<--' + str(itr.val) + '-->'
            itr = itr.next
        print(list1)
        return
    def traverse_backword(self):
        if self.tail is None:
            print('Linked List Is Empty')
            return
        current = self.tail
        l2 = ''
        while current:
            l2 += '<--' + str(current.val) + '-->'
            current = current.prev

        print(l2)
        return

if __name__ == '__main__':
    l1 = DoublyLinkedList()
    l1.insert_at_head(4)
    l1.insert_at_head(3)
    l1.insert_at_head(2)
    l1.insert_at_tail(5)
    l1.traverse_forward()
    # l1.delete_at_head()
    # l1.traverse_forward()
    # l1.delete_at_tail()
    # l1.traverse_backword()
    l1.insert_at_position(1,1)
    l1.traverse_forward()
    l1.search(5)
    print(l1.get_head())
    print(l1.get_tail())
    print(l1.get_size())
    
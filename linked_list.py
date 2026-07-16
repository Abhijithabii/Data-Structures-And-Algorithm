class Node:
    def __init__(self, data = None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_data_beginning(self,data):
        node = Node(data,self.head)
        self.head = node

    def show_linked_list(self):
        if self.head is None:
            print('Linked List is Empty')
            return
        itr = self.head
        list1 = ''
        while itr:
            list1 += str(itr.data) + '-->'
            itr = itr.next
        print(list1)
            
        return
    def insert_at_end(self,data):
        node  = Node(data)
        if self.head is None:
            self.head = node
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = node
    def insert_fresh_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
            
    def add_at_index(self, data , idx):
        node = Node(data)
        if idx == 0:
            node.next = self.head
            self.head = node
        count = 1
        itr = self.head
        while itr.next:
            itr = itr.next
            count += 1
            if count == idx:
                temp = itr.next
                itr.next = node
                node.next = temp
                return
        else:
            print("index out of range")
            return
            
    def delete_at_index(self,idx):
        if idx == 0:
            if self.head.next is None:
                self.head = None

            else:
                self.head = self.head.next

            return
        count = 1
        itr = self.head
        while itr.next:
            itr = itr.next
            count += 1
            if count == idx:
                itr.next = itr.next.next
                return
        else:
            print('Index Out of range')
            return

    def get_index(self,idx):
        itr = self.head
        counter = 0
        while itr.next:
            if counter == idx:
                print( itr.data)
                return 
            itr = itr.next
            counter += 1


    def insert_after_value(self,data_after, data_to_insert):
        
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                return
            itr = itr.next
        return
    # search for first occurance of data after value in linked list
    # now insert the data to insert after the data after


    def remove_by_value(self, remove_value):
        # remove first node that contain the value to be removed
        pass

    def reverse_linked_list(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        itr = self.head
        list2 = ''
        while itr.next:
            prev = itr
            next_itr = itr.next
            itr.next = None



    
    

if __name__ == '__main__':
    l1 = LinkedList()
    l1.insert_fresh_values([1,2,3,4,5,6,7,8,9])
    l1.add_at_index(10,2)
    l1.show_linked_list()
    l1.delete_at_index(5)
    l1.show_linked_list()
    l1.get_index(5)
    l1.insert_after_value(9,11)
    l1.show_linked_list()
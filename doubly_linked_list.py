class Node:
    def __init__(self, item):
        self.prev= None
        self.next = None
        self.value = item
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, item):
        print(f"Inserting item {item} at the begining")
        new_node = Node(item)
        # check if empty list
        if(self.head is None):
            self.head = new_node
            return
        else:
            cur_head = self.head
            cur_head.prev = new_node
            new_node.next = cur_head
            self.head = new_node

    def insert_after(self, prev_item, item):
        new_node = Node(item)
        print(f"insert item {item} after {prev_item}")
        # check if empty list
        if(self.head is None):
            print("Empty list, exiting")
        # otherwise add the item with a traversing, check if last node, then add after it
        linkedlist = self.head
        while(linkedlist != None):
            "If last item"
            if(linkedlist.next is None):
                new_node.prev = linkedlist
                linkedlist.next = new_node
                break
            elif(linkedlist.value == prev_item):
                next_item = linkedlist.next
                new_node.next = next_item
                new_node.prev = linkedlist
                linkedlist.next = new_node
                if next_item:
                    next_item.prev = new_node
                break
            linkedlist = linkedlist.next

    def insert_at_last(self, item):
        print(f"Inserting item {item} at the end")
        new_node = Node(item)       

        # check if empty queue
        if self.head is None:
            self.head = new_node
            return

        linkedlist = self.head
        while linkedlist != None:
            # check for last item
            if(linkedlist.next is None):
                new_node.prev = linkedlist
                linkedlist.next = new_node
                break
            else:
                linkedlist = linkedlist.next

    def delete_item(self, item):
        print(f"delete item {item}")
        #if empty list
        if(self.head is None):
            print("Empty list, exiting")
        # if single element
        if(self.head.next is None):
            self.head = None
            return
        # traverse and delete
        linkedlist = self.head
        while linkedlist is not None:
            
            if(linkedlist.value == item):
                #check if first item
                if(linkedlist.prev is None):                
                    next_item = linkedlist.next                
                    next_item.prev = None
                    self.head = next_item
                    break
                #check if last item
                elif(linkedlist.next is None):
                    prev_item = linkedlist.prev
                    prev_item.next = None
                    break
                else:
                    prev_item = linkedlist.prev
                    next_item = linkedlist.next
                    linkedlist.prev.next = next_item
                    break
            linkedlist = linkedlist.next

    def __str__(self):
        values = [str(value) for value in self]
        return " <-> ".join(values)

    def __len__(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

    def __iter__(self):
        self._iter_node = self.head  # Start from the head
        return self                  # Return the iterator (the list itself)

    def __next__(self):
        if self._iter_node is None:
            raise StopIteration      # End of list reached
        value = self._iter_node.value
        self._iter_node = self._iter_node.next  # Move to next node
        return value    

dll = DoublyLinkedList() 
dll.insert_at_begining(2)
print(dll)  
dll.insert_at_begining(3)
print(dll) 
dll.insert_at_last(4)
print(dll) 
dll.insert_after(2, 6)
print(dll) 
dll.insert_after(4, 9)
print(dll) 
dll.delete_item(6)
print(dll) 
dll.delete_item(3)
print(dll) 
dll.delete_item(9)
print(dll) 
dll.delete_item(4)
print(dll) 
dll.delete_item(2)
print(dll) 


""" print("Length:", len(dll))         

print("Items:")
for item in dll:
    print(item) """
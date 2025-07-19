class Node:
    def __init__(self, item):
        self.value = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
linkedListObj = LinkedList()

firstObj = Node(1)
secObj = Node(2)
thirdObj = Node(3)

linkedListObj.head = firstObj
linkedListObj.head.next = secObj
secObj.next = thirdObj

while linkedListObj.head != None:
    print(linkedListObj.head.value)
    linkedListObj.head = linkedListObj.head.next

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None
class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.tail.prev == self.head
        

    def append(self, value: int) -> None:
        newnode= Node(value)
        prev_node = self.tail.prev
        prev_node.next = newnode
        self.tail.prev = newnode
        newnode.next = self.tail
        newnode.prev = prev_node
        

    def appendleft(self, value: int) -> None:
        newnode = Node(value)
        sec_node = self.head.next
        sec_node.prev = newnode
        self.head.next = newnode
        newnode.next = sec_node
        newnode.prev = self.head
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        prev_node = self.tail.prev
        prev_val = prev_node.val
        last_node = prev_node.prev
        last_node.next = self.tail
        self.tail.prev = last_node
        return prev_val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        first_node = self.head.next 
        first_val = first_node.val
        second_node = first_node.next
        second_node.prev = self.head
        self.head.next = second_node
        return first_val
        

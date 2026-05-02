class ListNode:
    def __init__(self,val,Nextnode = None):
        self.next = Nextnode 
        self.val = val


class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1
        

    def insertHead(self, val: int) -> None:
        new = ListNode(val)
        new.next = self.head.next
        self.head.next = new
        if not new.next:
            self.tail = new

        

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next
        

    def remove(self, index: int) -> bool:
        curr = self.head
        i = 0 
        while i < index and curr:
            i += 1
            curr = curr.next 
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr 
            curr.next = curr.next.next
            return True 
        return False

    def getValues(self) -> List[int]:
        curr = self.head.next
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res

        

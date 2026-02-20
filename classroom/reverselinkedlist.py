class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def reverseList(self, head):
        p = None
        while head:
            t = head
            head = head.next
            t.next = p
            p = t
        return p
    
    def printList(head):
        while head:
            print(head.val, end=" -> ")
            head = head.next
        print("None")


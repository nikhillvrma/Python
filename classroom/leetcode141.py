# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        
        fp = sp = head
        while fp:
            sp = sp.next
            if fp.next == None:
                return False
            fp = fp.next.next
            if sp == fp:
                return True
        return False
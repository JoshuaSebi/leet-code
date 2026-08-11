class ListNode:
    def __init__(self, data=0, next=None):
        self.data=data
        self.next=next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        
        prev=dummy
        while prev.next and prev.next.next:
            first=prev.next
            second=first.next

            first.next=second.next
            prev.next=second
            second.next=first

            prev=first
        return dummy.next
        
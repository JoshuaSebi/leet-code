# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dixt1={}
        a=head
        while a:
            if a in dixt1:
                return True
            dixt1[a]=1
            a=a.next
        return False
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        # basically have 2 LinkedList and append to them based on value
        # O(N)

        left,right=ListNode(),ListNode() # basically dummy nodes so there next is supposed to have values
        ltail,rtail=left,right
        
        while head:
            if head.val<x:
                ltail.next=head
                ltail=ltail.next
            else:
                rtail.next=head
                rtail=rtail.next
            
            head=head.next
        
        # since we are done tarversing so left.next should point to start of right
        ltail.next=right.next # since right is a dummy node
        
        rtail.next=None # since the ending of a LL has to be None
        
        return left.next
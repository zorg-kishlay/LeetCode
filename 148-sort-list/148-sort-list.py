# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # basically doing merge sort for linked list
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        left=head
        right=self.getMid(head)
        tmp= right.next
        right.next=None
        right=tmp
        
        left=self.sortList(left)
        right = self.sortList(right)
        return self.merge(left,right)
    
    def getMid(self,head):
        slow,fast=head,head.next
        
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        return slow
    
    def merge(self,l1,l2):
        dummy=ListNode()
        tmp=dummy
        
        while l1 and l2:
            if l1.val<l2.val:
                tmp.next=l1
                l1=l1.next
            
            else:
                tmp.next=l2
                l2=l2.next
            
            tmp=tmp.next
        
        if l1:
            tmp.next=l1
        
        if l2:
            tmp.next=l2
        
        return dummy.next
        
        
        
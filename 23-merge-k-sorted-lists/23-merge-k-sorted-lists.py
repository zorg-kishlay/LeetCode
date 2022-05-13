# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        #O(NlogK)
        
        # sample of merge step of merge sort
        # we will keep dividing k list into pairs of linked list (logK) and merge the 2 linked list
        # so n*logK
        
        if not lists or len(lists)==0:
            return None
        
        while len(lists)>1:
            merged_list = []
            for i in range(0,len(lists),2):
                l1=lists[i]
                l2 = lists[i+1] if (i+1)<len(lists) else None
                merged_list.append(self.mergetwo(l1,l2))
            
            lists = merged_list
        return lists[0]
        
    
    def mergetwo(self,l1,l2):
        dummy=ListNode()
        tail = dummy
        
        while l1 and l2:
            if l1.val<l2.val:
                tail.next=l1
                l1=l1.next
            else:
                tail.next=l2
                l2=l2.next
            
            tail=tail.next
       
    # equivqlent of gather stage
        if l1:
            tail.next=l1
        
        if l2:
            tail.next=l2

        
        return dummy.next
            
                
                
                
                
            
        
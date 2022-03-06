# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        # Approach 1 calculate the diff b/w lengths of both lists and traverse the longer 
        # list till the diff and then start traversing both lists comparing nodes
        
        # Approach 2 traverse both lists and when you reach at the end of list1 start iterating over
        # list 2 similar to above we go by len(list1)+len(list2) steps
        
        list1, list2 = headA, headB
        
        while list1 != list2:
            list1 = list1.next if list1 else headB
            list2 = list2.next if list2 else headA
        
        
        return list1 # or list2 doesn’t matter
    # also covers when they don’t have an intersection these 2 will be equal at None
            
        
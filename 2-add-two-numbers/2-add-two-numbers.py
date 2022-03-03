# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # create a dummy node to make use of
        dummy = ListNode()
        
        current = dummy
        carry = 0
        #while l1 or l2: # with this we miss the part where lets say 7+3 so we need to check for carry as well
        while l1 or l2 or carry:
            value1 = l1.val if l1 else 0 # since addition adding to 0 is no issues
            value2 = l2.val if l2 else 0
            
            sum_value = value1 + value2 + carry
            
            carry = sum_value // 10 # gives us tens/carry value in case of a 2 digit number
            
            sum_value = sum_value % 10 # gives us ones digit since we will insert that into the linked list
            
            current.next = ListNode(sum_value)
        
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        
        return dummy.next
            
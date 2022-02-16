# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1,head)
        first = dummy
        second = first.next

        while second is not None and first is not None:
            prev = first.next
            if second.next is None:
                break
            sec= second.next.next
            first.next = second.next
            second.next.next = prev
            second.next = sec
            #prev = fir
            first = first.next.next

            second = first.next

        return dummy.next
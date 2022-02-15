# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseL(self, curr, prev, last):
        if curr is last:
            return prev
        nex = curr.next
        curr.next = prev
        return self.reverseL(nex, curr, last)

    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = slow = head

        while (fast is not None):
            fast = fast.next.next
            slow = slow.next

        # one reverse list from starting to middle
        # and other from middle to end
        l1 = self.reverseL(head, None, slow)
        l2 = slow
        val = 0

        # so for [5,4,2,1]
        # l1= [5,4] since slow would be at 4 only
        # l2 = [1,2]
        while l1 is not None and l2 is not None:
            val = max(val, l1.val + l2.val)
            l1 = l1.next
            l2 = l2.next

        return val
        
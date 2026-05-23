# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#this is just a normal solution to problem 2 (this is my first time working with liked list so i got a little help from llm)
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        current = dummy
        holder = 0

        while l1 is not None or l2 is not None:
            
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0

            total = val1 + val2 + holder
            if total >= 10:
                current.next = ListNode(total % 10)
                holder = 1
                
            else:
                current.next = ListNode(total)
                holder = 0
                
            current = current.next
    
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        if holder > 0:
            current.next = ListNode(1)


        return dummy.next

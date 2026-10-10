# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        n_nodes = 0
        while current:
            n_nodes+=1
            current = current.next
        
        n_from_end_i = n_nodes - n+1

        dummy = ListNode(0, head)
        pointer = dummy
        index = 0
        while pointer:
            if index == n_from_end_i-1:
                pointer.next = pointer.next.next
                break
            pointer = pointer.next
            index+=1
        return dummy.next
        
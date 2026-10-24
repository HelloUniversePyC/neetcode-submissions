# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        fast,slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        

        ## Reverse second half
        prev = None
        curr_node = slow.next
        slow.next = None

        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev
            prev = curr_node
            curr_node = next_node

        #Combine:
    
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            
            first.next = second
            second.next = tmp1
            
            first = tmp1
            second = tmp2

        

       
            

        
        
        
        
                

        

        
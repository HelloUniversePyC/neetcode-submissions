# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        left = list1
        right = list2
        starter_node = ListNode(0,None)
        output_list = starter_node
        #Handle nodes within same length
        while(left and right):
            if right.val < left.val:
                output_list.next = right
                right = right.next
            else:
                output_list.next = left
                left = left.next
            output_list = output_list.next
        #Remaining left nodes
        while(left):
            output_list.next = left
            left = left.next
            output_list = output_list.next
        #Remining right nodes
        while(right):
            output_list.next = right
            right = right.next
            output_list = output_list.next
        return starter_node.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #Naive solution

        #Loop first list get #
        pointer1 = l1
        number1 = ""
        while pointer1:
            number1+=str(pointer1.val)
            pointer1 = pointer1.next
        number1 = number1[::-1]


        #Loop second list get #
        pointer2 = l2
        number2 = ""
        while pointer2:
            number2+=str(pointer2.val)
            pointer2 = pointer2.next
        number2 = number2[::-1]
        #Sum
        total = int(number1) + int(number2)
        total = str(total)[::-1]
        #Create linked list representing total

        dummy = ListNode(0)
        current = dummy
        for digit in total:
            current.next = ListNode(int(digit))
            current = current.next
        return dummy.next


        
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr_node = head
        direc = {None:None}
        while curr_node:
            direc[curr_node] = Node(curr_node.val)
            curr_node = curr_node.next
        
        cur = head
        while(cur):
            copy = direc[cur]
            copy.next = direc[cur.next]
            copy.random = direc[cur.random]
            cur = cur.next

        return direc[head]
        

        
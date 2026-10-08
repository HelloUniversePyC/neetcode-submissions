# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = k
        def inorder(node):
            nonlocal count
            if not node:
                return None
            left = inorder(node.left)
            # check left
            if left is not None:
                return left
            # Process current
            count = count-1
            if count == 0:
                return node.val
            #go right, check right
            right = inorder(node.right)
            if right is not None:
                return right
        return inorder(root)

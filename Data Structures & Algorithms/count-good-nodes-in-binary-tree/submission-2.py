# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def count_good_nodes(node, max_seen):
            if not node:
                return 0
            if node.val >= max_seen:
                max_seen = node.val
                return 1 + count_good_nodes(node.left, max_seen)+count_good_nodes(node.right, max_seen)
            return count_good_nodes(node.left, max_seen)+count_good_nodes(node.right, max_seen)
        return count_good_nodes(root, root.val)
            
            

        
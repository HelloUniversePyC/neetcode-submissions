# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque()
        q.append(root)
        right_view = []
        while q:
            level_size = len(q)
            curr_lev = []
            for i in range(level_size):
                n = q.popleft()
                if i == (level_size-1):
                    right_view.append(n.val)
                if n.left is not None:
                    q.append(n.left)
                if n.right is not None:
                    q.append(n.right)
        return right_view
from collections import deque

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self
        if root is None:
            return -1
        res=[]
        def bfs(root):
            q=deque([root])
            while q:
                level=[]
                for i in range(len(q)):
                    node=q.popleft()
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                res.append(sum(level))
        bfs(root)
        if len(res)<k:
            return -1
        
        res.sort()
        return res[-k]
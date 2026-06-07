# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def createBinaryTree(self, descriptions):
        
        mp = {}
        children = set()

        for parent, child, isLeft in descriptions:
            if parent not in mp: mp[parent] = TreeNode(parent)
            if child not in mp: mp[child] = TreeNode(child)

            if isLeft:
                mp[parent].left = mp[child]
            else:
                mp[parent].right = mp[child]

            children.add(child)

        for parent, child, isLeft in descriptions:
            if parent not in children:
                return mp[parent]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#DFS APPROACH
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.isSametree(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

    def isSametree(self, t1,t2):
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None or t1.val!=t2.val:
            return False
        return self.isSametree(t1.left,t2.left) and self.isSametree(t1.right,t2.right)
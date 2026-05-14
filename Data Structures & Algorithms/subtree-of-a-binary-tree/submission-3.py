# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        tree=self.serialize(root)
        subtree=self.serialize(subRoot)
        if subtree in tree:
            return True
        else:
            return False
    def serialize(self,tree):
        if tree is None:
            return "$#"
        return ("$"+str(tree.val)+self.serialize(tree.left)+self.serialize(tree.right))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #BFS
        pq=deque([p])
        qq=deque([q])
        while pq and qq:
            #for i in range(len(pq)):
            pnode=pq.popleft()
            qnode=qq.popleft()
            if pnode is None and qnode is None:
                continue
            if pnode is None or qnode is None or pnode.val!=qnode.val:
                return False
            pq.append(pnode.left)
            pq.append(pnode.right)
            qq.append(qnode.left)
            qq.append(qnode.right)
                
        return True
            

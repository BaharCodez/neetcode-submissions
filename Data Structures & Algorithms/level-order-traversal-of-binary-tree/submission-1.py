# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q = deque([root])
        ans = [] 
        if not root:
            return ans
        while q:
            
            level = len(q) 
            loop = []
            for i in range(level):
                l = q[0]
                if l.left:
                    q.append(l.left)
                if l.right:
                    q.append(l.right)
                loop.append(l.val)
                q.popleft()

            ans.append(loop)    
        
        return ans



                



            

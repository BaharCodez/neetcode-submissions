# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Traverse downright side
        # If no right side root, then traverse back up until left root avail
        if not root:
            return []
        

        q = deque([root])
        ans = []
        
        while q:
            level = len(q)
            loop = []
            for i in range(level):

                num = q.popleft()
                loop.append(num.val)

                if num.left:
                    q.append(num.left)
                if num.right:
                    q.append(num.right)

            ans.append(loop[-1])

        return ans

                




            
                
        

        
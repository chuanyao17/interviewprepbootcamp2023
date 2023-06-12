# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        
        output=[]
        queue=deque([root])
        dirr=1
        while queue:
            cur_len=len(queue)
            cur_level=deque()
            for _ in range(cur_len):
                node=queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
                if dirr==1:
                    cur_level.append(node.val)
                if dirr==-1:
                    cur_level.appendleft(node.val)
                    
            output.append(cur_level)
            dirr*=-1
        return output
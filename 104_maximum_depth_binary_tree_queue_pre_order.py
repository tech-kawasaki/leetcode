from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root) -> int:
        queue = deque()
        if root is not None:
            queue.append((1,root))
        
        depth = 0
        while queue:
            current_depth, root = queue.popleft()
            if root is not None:
                depth = max(depth, current_depth)
                queue.append((current_depth + 1, root.left))
                queue.append((current_depth + 1, root.right))
                
        return depth
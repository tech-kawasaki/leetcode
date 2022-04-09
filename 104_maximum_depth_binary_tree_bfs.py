from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        count = 0
        if root == None:
            return count
        queue.append(root)
        while (len(queue)):
            count += 1
            for i in range(len(queue)):
                current = queue.popleft()
                if current.left != None:
                    queue.append(current.left)
                if current.right != None:
                    queue.append(current.right)
                
        return count
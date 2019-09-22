# Leetcode problem: Find Largest Value in Each Tree Row (515)

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def merge(self, a: List[int], b: List[int]) -> List[int]:
        c = []
        for i in range(0, min(len(a), len(b))):
            c.append(max(a[i], b[i]))
        if len(a) >= len(b):
            c.extend(a[len(b):])
        else:
            c.extend(b[len(a):])
        return c
    
    def largestValues(self, root: TreeNode) -> List[int]:
        s = Solution()
        if root == None:
            return []
        values = [root.val]
        if root.left:
            values = s.merge(values, [root.val]+s.largestValues(root.left))
        if root.right:
            values = s.merge(values, [root.val]+s.largestValues(root.right))
        return values

s = Solution()
root = TreeNode(1)
l = TreeNode(3)
r = TreeNode(2)
ll = TreeNode(5)
lr = TreeNode(3)
rr = TreeNode(9)
l.left = ll
l.right = lr
r.right = rr
root.left = l
root.right = r
print(s.largestValues(root))

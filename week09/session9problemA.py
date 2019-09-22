# Leetcode problem: Maximum Depth of Binary Tree (104)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        depths = [(root, 1)]
        maxD = 1
        while depths:
            i = depths.pop()
            maxD = max(maxD, i[1])
            if i[0].left:
                depths.append((i[0].left, i[1]+1))
            if i[0].right:
                depths.append((i[0].right, i[1]+1))
        return maxD

s = Solution()
root = TreeNode(3)
l = TreeNode(9)
r = TreeNode(20)
rl = TreeNode(15)
rr = TreeNode(7)
r.left = rl
r.right = rr
root.left = l
root.right = r
print(s.maxDepth(root))

# Leetcode problem: Minimum Depth of Binary Tree (111)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        depths = [(root, 1)]
        minD = -1
        while depths:
            i = depths.pop()
            if not (i[0].left or i[0].right):
                if minD == -1:
                    minD = i[1]
                else:
                    minD = min(minD, i[1])
            if i[0].left:
                depths.append((i[0].left, i[1]+1))
            if i[0].right:
                depths.append((i[0].right, i[1]+1))
        return minD

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
print(s.minDepth(root))

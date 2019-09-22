# Leetcode problem: Maxiumum Difference Between Node and Ancestor (1026)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    global maxDifference
    maxDifference = 0
    
    def helper(self, node: TreeNode, highest: int, lowest: int) -> None:
        global maxDifference
        s = Solution()
        if highest - node.val > maxDifference:
            maxDifference = highest - node.val
        if node.val - lowest > maxDifference:
            maxDifference = node.val - lowest
        if node.left:
            s.helper(node.left, max(highest, node.val), min(lowest, node.val))
        if node.right:
            s.helper(node.right, max(highest, node.val), min(lowest, node.val))
    
    def maxAncestorDiff(self, root: TreeNode) -> int:
        global maxDifference
        maxDifference = 0
        s = Solution()
        s.helper(root, -1, 100001)
        return maxDifference

s = Solution()
root = TreeNode(8)
l = TreeNode(3)
r = TreeNode(10)
ll = TreeNode(1)
lr = TreeNode(6)
rr = TreeNode(14)
lrl = TreeNode(4)
lrr = TreeNode(7)
rrl = TreeNode(13)
lr.left = lrl
lr.right = lrr
rr.left = rrl
l.left = ll
l.right = lr
r.right = rr
root.left = l
root.right = r
print(s.maxAncestorDiff(root))

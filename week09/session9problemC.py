# Leetcode problem: Path Sum (112)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return False
        nodes = [(root, sum)]
        while nodes:
            i = nodes.pop()
            if i[0].left:
                nodes.append((i[0].left, i[1]-i[0].val))
            if i[0].right:
                nodes.append((i[0].right, i[1]-i[0].val))
            if (i[0].val == i[1]) and not (i[0].left or i[0].right):
                return True
        return False

s = Solution()
root = TreeNode(5)
l = TreeNode(4)
r = TreeNode(8)
ll = TreeNode(11)
rl = TreeNode(13)
rr = TreeNode(4)
lll = TreeNode(7)
llr = TreeNode(2)
rrr = TreeNode(1)
ll.left = lll
ll.right = llr
rr.right = rrr
l.left = ll
r.left = rl
r.right = rr
root.left = l
root.right = r
print(s.hasPathSum(root, 22))

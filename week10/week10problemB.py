# Leetcode problem: Delete Nodes And Return Forest (1110)
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    global forest
    forest = []
    
    def helper(self, node: TreeNode, to_delete: List[int], parent: TreeNode, side: str) -> None:
        global forest
        s = Solution()
        if ((parent == None) or (parent.val in to_delete)) and not (node.val in to_delete):
            forest.append(node)
        if node.left:
            a = s.helper(node.left, to_delete, node, "l")
        if node.right:
            b = s.helper(node.right, to_delete, node, "r")
        if node.val in to_delete:
            if parent:
                if side == "l":
                    parent.left = None
                else:
                    parent.right = None
            node = None

    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        global forest
        forest = []
        s = Solution()
        a = s.helper(root, to_delete, None, "l")
        return forest
            
s = Solution()
root = TreeNode(1)
l = TreeNode(2)
r = TreeNode(3)
ll = TreeNode(4)
lr = TreeNode(5)
rl = TreeNode(6)
rr = TreeNode(7)
l.left = ll
l.right = lr
r.left = rl
r.right = rr
root.left = l
root.right = r
print([i.val for i in s.delNodes(root, [3, 5])])

# input [1, 2, null, 4, 3], [2, 3]
# output [1, 4, 3]
# should be [1, 4]

# Leetcode problem: Binary Tree Level Order Traversal (102)

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        nodes = [(0, root)]
        storage = [(0, root.val)]
        while nodes:
            i = nodes.pop(0)
            if i[1].left:
                nodes.append((i[0]+1, i[1].left))
                storage.append((i[0]+1, i[1].left.val))
            if i[1].right:
                nodes.append((i[0]+1, i[1].right))
                storage.append((i[0]+1, i[1].right.val))
        ans = []
        for i in storage:
            if len(ans) <= i[0]:
                ans.append([i[1]])
            else:
                ans[i[0]].append(i[1])
        return ans

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
print(s.levelOrder(root))

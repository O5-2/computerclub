# Leetcode problem: Lowest Common Ancestor of Deepest Leaves (1123)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    seen_nodes = set()
    
    def helper(self, start_node: TreeNode, depth: int) -> int:
        global seen_nodes
        s = Solution()
        seen_nodes.add(start_node)
        if not (start_node.left or start_node.right):
            return (start_node, depth)
        elif not start_node.right:
            l = s.helper(start_node.left, depth+1)
            return l
        elif not start_node.left:
            r = s.helper(start_node.right, depth+1)
            return r
        else:
            l = s.helper(start_node.left, depth+1)
            r = s.helper(start_node.right, depth+1)
            if r[1] > l[1]:
                return r
            elif r[1] == l[1]:
                return (start_node, r[1])
            else:
                return l
            
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        global seen_nodes
        s = Solution()
        seen_nodes = set()
        return s.helper(root, 1)[0]

s = Solution()
Aroot = TreeNode(1)
Al = TreeNode(2)
Ar = TreeNode(3)
Aroot.left = Al
Aroot.right = Ar
print(s.lcaDeepestLeaves(Aroot))
Broot = TreeNode(1)
Bl = TreeNode(2)
Br = TreeNode(3)
Bll = TreeNode(4)
Bl.left = Bll
Broot.left = Bl
Broot.right = Br
print(s.lcaDeepestLeaves(Broot))
Croot = TreeNode(1)
Cl = TreeNode(2)
Cr = TreeNode(3)
Cll = TreeNode(4)
Clr = TreeNode(5)
Cl.left = Cll
Cl.right = Clr
Croot.left = Cl
Croot.right = Cr
print(s.lcaDeepestLeaves(Croot))

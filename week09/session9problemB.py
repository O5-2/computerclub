# Leetcode problem: Same Tree (100)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if (p == None) and (q == None):
            return True
        elif (p == None) or (q == None):
            return False
        pNodes = [p]
        qNodes = [q]
        while pNodes:
            i = pNodes.pop()
            j = qNodes.pop()
            if i.val != j.val:
                return False
            if (bool(i.left) ^ bool(j.left)):
                return False
            if (bool(i.right) ^ bool(j.right)):
                return False
            if i.left:
                pNodes.append(i.left)
                qNodes.append(j.left)
            if i.right:
                pNodes.append(i.right)
                qNodes.append(j.right)
        return True

s = Solution()
AProot = TreeNode(1)
APl = TreeNode(2)
APr = TreeNode(3)
AProot.left = APl
AProot.right = APr
AQroot = TreeNode(1)
AQl = TreeNode(2)
AQr = TreeNode(3)
AQroot.left = AQl
AQroot.right = AQr
print(s.isSameTree(AProot, AQroot))
BProot = TreeNode(1)
BPl = TreeNode(2)
BProot.left = BPl
BQroot = TreeNode(1)
BQr = TreeNode(2)
BQroot.right = BQr
print(s.isSameTree(BProot, BQroot))
CProot = TreeNode(1)
CPl = TreeNode(2)
CPr = TreeNode(1)
CProot.left = CPl
CProot.right = CPr
CQroot = TreeNode(1)
CQl = TreeNode(1)
CQr = TreeNode(2)
CQroot.left = CQl
CQroot.right = CQr
print(s.isSameTree(CProot, CQroot))

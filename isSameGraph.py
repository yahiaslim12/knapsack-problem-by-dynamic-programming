class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        first = self.check(p,'R')  
        if first == self.check(q,'R'):
            return True
        else:
            return False

    def check(self, node,side):
        if node is None:
            return []
        else:
            return  self.check(node.left,'l') + [(node.val,side)] + self.check(node.right,'r') 

sol = Solution()
tree1 = TreeNode(val=1, left=TreeNode(1))
tree2 = TreeNode(val=1, left=TreeNode(1))
res = sol.isSameTree(tree1, tree2)
print(res)

# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isValidBST(self, A):
        if A.left == None and A.right == None:
            return 1
        elif A.left == None:
            if A.val < A.right.val:
                return self.isValidBST(A.right)
            else:
                return 0
        elif A.right == None:
            if A.val > A.left.val:
                return self.isValidBST(A.left)
            else:
                return 0
        elif A.left.val > A.val:
            return 0
        elif A.right.val < A.val:
            return 0
        elif self.isValidBST(A.left) == 0:
            return 0
        elif self.isValidBST(A.right) == 0:
            return 0
        return 1

if __name__ == '__main__':
    A = TreeNode(11)
    A.right = TreeNode(2)
    A.left = TreeNode(4)
    A.left.left = TreeNode(5)
    A.left.right = TreeNode(1)
    A.right.left = TreeNode(5)
    S = Solution()
    print S.isValidBST(A)
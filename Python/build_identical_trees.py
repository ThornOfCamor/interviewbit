# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    def numEle(self, A):
        if A == None:
            return 0
        else:
            return self.numEle(A.left) + 1 + self.numEle(A.right)

    def cntMatrix(self, A, B, flag = 0):
        a = self.numEle(A)
        b = self.numEle(B)
        if a >= b and flag == 0:
            return -1
        if a > b:
            return -1
        if A == None:
            return b
        al = self.numEle(A.left)
        ar = self.numEle(A.right)
        bl = self.numEle(B.left)
        br = self.numEle(B.right)
        if al > bl or ar > br:
            return -1
        if A.right == None:
            if A.left == None:
                return b-1
            else:
                if self.numEle(B.left.right) > A.val-A.left.val-1:
                    return -1
                else:
                    return self.cntMatrix(A.left, B.left)
        if A.left == None:
            if self.numEle(B.right.left) > A.right.val - A.val:
                return -1
            else:
                return self.cntMatrix(A.right, B.right)
        c = self.cntMatrix(A.left, B.left, 1)
        d = self.cntMatrix(A.right, B.right, 1)
        if c == -1 or d == -1:
            return -1
        else:
            return c + d

if __name__ == '__main__':
    A = TreeNode(10)
    A.left = TreeNode(9)
    A.right = TreeNode(20)
    B = TreeNode(5)
    B.left = TreeNode(2)
    B.left.left = TreeNode(1)
    B.right = TreeNode(7)
    S = Solution()
    C = S.cntMatrix(A, B)
    print C

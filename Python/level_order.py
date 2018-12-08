# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def levelOrder(self, A):
        if A is None:
            return []
        if A.right == None:
            if A.left == None:
                return [[A.val]]
            else:
                ans = [[A.val]]
                ans.extend(self.levelOrder(A.left))
                return ans
        elif A.left == None:
            ans = [[A.val]]
            ans.extend(self.levelOrder(A.right))
            return ans
        queuecurr = [A]
        queuenext = []
        ans = []
        row = []
        while queuecurr != []:
            while queuecurr != []:
                curr = queuecurr[0]
                row.append(curr.val)
                if curr.left is not None:
                    queuenext.append(curr.left)
                if curr.right is not None:
                    queuenext.append(curr.right)
                queuecurr.pop(0)
            ans.append(row)
            row = []
            queuecurr = queuenext
            queuenext = []
        return ans
        
if __name__ == '__main__':
    A = TreeNode(1)
    A.left = TreeNode(5)
    S = Solution()
    B = []
    B = S.levelOrder(A)
    print B


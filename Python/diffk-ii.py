class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        if len(A) <= 1:
            return 0
        C = []
        a = max(A) - min(A)
        if B > a:
            return 0
        elif B == a:
            return 1
        while a >= 0:
            C.append(0)
            a  = a - 1
        x = 0
        while x < len(A)-1:
            y = x + 1
            while y < len(A):
                if A[x]>=A[y]:
                    C[A[x]-A[y]] = C[A[x]-A[y]] + 1
                elif A[y]>A[x]:
                    C[A[y]-A[x]] = C[A[y]-A[x]] + 1
                y = y + 1
            x = x + 1
        print C
        if C[B] == 0:
            return 0
        else:
            return 1

    
if __name__ == '__main__':
    S = Solution()
    C = S.diffPossible([1, 3, 1, 6], 0)
    print C
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        x = 0
        n = len(A)
        if A[n-1] == 0:
            return 1
        while x < n-1:
            if A[x] == n - 1 - x and A[x] != A[x+1]:
                return 1
            x = x + 1
        return -1

if __name__ == '__main__':
    S = Solution()
    A = raw_input()
    B = A.split(" ")
    C = []
    for x in B:
        C.append(int(x, 10))
    D = S.solve(C)
    print D
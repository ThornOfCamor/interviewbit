class Solution:
    # @param A : list of integers
    # @return a list of integers
    def lexoCompare(self, A, B):
        C = []
        for x in A:
            C.append(x)
        D = []
        for x in B:
            D.append(x)
        for x in range(len(A)):
            if A[x]>B[x]:
                return D
            elif B[x]>A[x]:
                return C

    def smallestPair(self, A):
        D = []
        for x in range(len(A)):
            for y in range(x+1, len(A)):
                if A[x][1] != A[y][0] and A[x][1] != A[y][1] and A[x][0] < A[y][0]:
                    D.extend(A[x])
                    D.extend(A[y])
                    return D
        return D

    def equal(self, A):
        if len(A) < 4:
            return []
        a = 2*max(A)
        B = []
        while a >= 0:
            B.append([])
            a = a - 1
        x = 0
        while x < len(A)-1:
            y = x + 1
            while y < len(A):
                B[A[x]+A[y]].append([x, y])
                y = y + 1
            x = x + 1
        flag  = 0
        for a in B:
            if len(a) > 1:
                flag = 1
                break
        if flag == 0:
            return []
        curr = []
        best = [len(A), len(A), len(A), len(A)]
        flag = 0
        for x in B:
            if len(x)>1:
                curr = self.smallestPair(x)
                if len(curr)>0:
                    best = self.lexoCompare(best, curr)
                    flag = 1
        if flag == 0:
            return []
        else :
            return best

if __name__ == '__main__':
    S = Solution()
    A = S.equal([0, 1, 2, 3, 4, 5])
    print [0, 1, 2, 3, 4, 5]
    print A
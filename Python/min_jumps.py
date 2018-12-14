class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def minJumps(self, A, B):
        if B == 0:
            return []
        if B == 1:
            if -1 in A:
                return []
            else:
                return A
        n = len(A)
        if A[n-1] == -1:
            return []
        if n < 2:
            return [1]
        if n < 3:
            return [1, 2]
        lis = [[1]]
        num = [A[0]]
        x = 0
        while x < n-1:
            if A[x] != -1:
                y = x + 1
                m = B + y
                mini = min(m, n)
                while y < mini:
                    if len(lis) == y:
                        if A[y] != -1:
                            C = []
                            for z in lis[x]:
                                C.append(z)
                            C.append(y+1)
                            lis.append(C)
                            num.append(num[x] + A[y])
                        else:
                            lis.append([])
                            num.append(-1)
                    elif A[y] != -1 and num[y] > num[x] + A[y]:
                        C = []
                        for z in lis[x]:
                            C.append(z)
                        C.append(y+1)
                        lis[y] = C
                        num[y] = num[x] + A[y]
                    y += 1
            elif len(lis) == x:
                return []
            x += 1
        return lis[n-1]

if __name__ == '__main__':
    S = Solution()
    A = [ 248, 381 ]
    B = 6
    C = S.minJumps(A, B)
    print C

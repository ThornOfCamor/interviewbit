class Solution:
    # @param A : tuple of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        if n == 0:
            return 0
        ans = 1
        D = []
        x = 0
        while x < n-1:
            y = x + 1
            while y < n:
                count = 1
                d = A[y] - A[x]
                if d not in D:
                    count += 1
                    D.append(d)
                    z = y + 1
                    while z < n:
                        if A[z] - A[y] == d:
                            y = z
                            z = y + 1
                            count += 1
                        else:
                            z += 1
                if count > ans:
                    ans = count
                y += 1
            x += 1
        return ans

if __name__ == '__main__':
    S = Solution()
    A = [ 100, 10, 8, 300, 6, 1, 4, 2, 0]
    B = S.solve(A)
    print B

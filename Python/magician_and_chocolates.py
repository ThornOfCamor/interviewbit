class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def nchoc(self, A, B):
        b = len(B)
        ans = 0
        if b == 0:
            return 0
        if A == 0:
            return 0
        B.sort()
        if B[b -1] == 0:
            return (ans%(10**9 + 7))
        while A > 0:
            ans += B[b-1]
            c = int(B.pop()/2)
            if len(B) == 0:
                B.append(c)
            else:
                x = 0
                if c <= B[0]:
                    B.insert(0, c)
                else:
                    while x < b - 1:
                        if B[x] >= c:
                            B.insert(x, c)
                            break
                        x = x + 1
            A = A - 1
            if B[b-1] == 0:
                (ans%(10**9 + 7))
        return (ans%(10**9 + 7))
            
if __name__ == '__main__':
    S = Solution()
    A = [ 78, 46, 53, 43, 79, 46, 79, 80, 65, 81, 39, 84, 63, 24, 54, 42, 99, 15, 86, 45, 51, 47, 94, 35, 15, 30, 23 ]        
    B = 45
    C = S.nchoc(B, A)
    print C

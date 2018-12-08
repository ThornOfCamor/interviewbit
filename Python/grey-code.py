class Solution:
    # @param A : integer
    # @return a list of integers
    def dec_to_bin(self, x):
        return bin(x)[2:]
    
    def zero_extend(self, c):
        return "1" + c

    def change_bit(self, stra, p):
        B = list(stra)
        if B[p] == "1":
            B[p] = "0"
        else:
            B[p] = "1"
        c = ""
        for x in B:
            c = c + x
        return c
    
    def grey_code(self, A):
        if A == 0:
            return [0]
        if A == 1:
            return [0, 1]
        B = self.grey_code(A-1)
        c = self.dec_to_bin(B[len(B)-1])
        c = self.zero_extend(c)
        C = list(c)
        N = list(range(pow(2,A-1),pow(2,A)))
        Z = []
        for x in N:
            Z.append(self.dec_to_bin(x))
        B.append(int(c, 2))
        Z.pop(Z.index(c))
        while Z != []:
            i = 0
            while i < A:
                a = self.change_bit(c, i)
                if a in Z:
                    B.append(int(a, 2))
                    c = a
                    Z.pop(Z.index(a))
                    break
                i = i + 1
        return B
                    

    def grayCode(self, A):
        B = self.grey_code(A)
        return B

if __name__ == '__main__':
    S = Solution()
    A = 4
    B = S.grayCode(A)
    print B
    i = 0
    while i <= (2**4) -1:
        print S.dec_to_bin(B[i])
        i = i+1

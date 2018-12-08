class Solution:
    # @param A : integer
    # @param B : integer
    # @return a strings
    def nextdecimal(self, A, B):
        return str(int(10*A/B))
    
    def ToDecimal(self, A, B):
        C = []
        rem = []
        rem.append(A)
        x = self.nextdecimal(A, B)
        C.append(x)
        A = (10*A)%B
        if A == 0:
            a = "."
            for y in C:
                a = a + y   
            return a
        while A not in rem:
            print A
            rem.append(A)
            x = self.nextdecimal(A, B)
            C.append(x)
            A = (10*A)%B
            if A == 0:
                a = "."
                for y in C:
                    a = a + y   
                return a
        b = '.'
        a = ''
        for y in C:
            a = a + y
        b = b + a[0:rem.index(A)] + '(' + a[rem.index(A):] + ')'
        return b

    def fractionToDecimal(self, A, B):
        if B == 1:
            return str(A)
        if A == B:
            return '1'
        if A == 0:
            return '0'
        ans = ""
        if A < 0 and B < 0:
            return self.fractionToDecimal((-1)*A, (-1)*B)
        elif A < 0:
            return "-" + self.fractionToDecimal((-1)*A, B)
        elif B < 0:
            return "-" + self.fractionToDecimal(A, (-1)*B)
        if A > B and A%B == 0:
            return str(A/B)
        elif A > B:
            ans = str(int(A/B)) + self.ToDecimal(A%B, B)
            return ans
        else:
            return "0" + self.ToDecimal(A, B)
            
if __name__ == '__main__':
    S = Solution()
    A = S.fractionToDecimal(21, 22)
    print A
class Solution:
    # @param A : integer
    # @return a list of strings
    def Parens(self, A):
        C = []
        if A == 0:
            C.append("")
            return C
        if A == 1:
            C.append("()")
            return C
        i = 1;
        if A%2 == 0:
            while i <= A/2:
                D = self.Parens(i)
                E = self.Parens(A-i)
                for x in D:
                    for y in E:
                        if x+y not in C:
                            C.append(x+y)
                        if y+x not in C:
                            C.append(y+x)
                        j = 1
                        a = y
                        while j <= i:
                            a = '(' + a + ')'
                            j = j + 1
                        if a not in C:
                            C.append(a)
                    j = 1
                    a = x
                    while j <= A-i and i != A/2:
                        a = '(' + a + ')'
                        j = j + 1
                    if a not in C and i != A/2:
                        C.append(a)
                i = i + 1
        else: 
            while i <= (A-1)/2:
                D = self.Parens(i)
                E = self.Parens(A-i)
                for x in D:
                    for y in E:
                        if x+y not in C:
                            C.append(x+y)
                        if y+x not in C:
                            C.append(y+x)
                        j = 1
                        a = y
                        while j <= i:
                            a = '(' + a + ')'
                            j = j + 1
                        if a not in C:
                            C.append(a)
                    j = 1
                    a = x
                    while j <= A-i:
                        a = '(' + a + ')'
                        j = j + 1
                    if a not in C:
                        C.append(a)
                i = i + 1  
        return C
        
    def generateParenthesis(self, A):
        B = self.Parens(A)
        B.sort()
        return B

if __name__ == '__main__':
    A = 5
    B = []
    S = Solution()
    B = S.generateParenthesis(A)
    print B
    print len(B)

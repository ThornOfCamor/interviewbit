class Solution:
    # @param A : string
    # @return an integer
    def onlyDigits(self, A):
        for x in list(A):
            if x not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                return 0
        return 1

    def numOrDec(self, A):
        C = A.split(".")
        if len(C) == 1:
            if C[0][0] == "-":
                return self.onlyDigits(A[1:])
            else:
                return self.onlyDigits(A)
        if len(C) > 2:
            return 0
        if len(C) == 2:
            if C[1] == "":
                return 0
            if C[0] == "-":
                return 0
            if C[0] == "":
                return self.onlyDigits(C[1])
            elif C[0][0] == "-":
                if self.onlyDigits(C[0][1:]) == 1 and self.onlyDigits(C[1]) == 1:
                    return 1
                else :
                    return 0
            else:
                if self.onlyDigits(C[0]) == 1 and self.onlyDigits(C[1]) == 1:
                    return 1
                else:
                    return 0

    def isNumber(self, A):
        if A == "":
            return 0
        B = A.split(" ")
        x = 0
        while x < len(B):
            if B[x] == "":
                B.pop(x)
            else :
                x = x + 1
        if len(B) > 1:
            return 0
        if len(B) == 0:
            return 0
        C = B[0].split("e")
        if len(C) > 2:
            return 0
        if len(C) == 2:
            if C[0] == "" or C[0] == "-":
                return 0
            elif C[1] == "" or C[1] == "-":
                return 0
            else:
                if self.numOrDec(C[0]) == 1:
                    if C[1][0] == "-":
                        return self.onlyDigits(C[1][1:])
                    else:
                        return self.onlyDigits(C[1])
                else:
                    return 0
        return self.numOrDec(C[0])

if __name__ == '__main__':
    S = Solution()
    B = raw_input()
    A = S.isNumber(B)
    print A

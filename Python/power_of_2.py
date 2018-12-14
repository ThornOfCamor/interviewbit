class Solution:
    # @param A : string
    # @return an integer
    def power(self, A):
        if A == "1" or A == "0":
            return 0
        if A == "2" or A == "4" or A == "8":
            return 1
        B = list(A)
        b = len(B)
        if int(B[b-1],10)%2 == 1:
            return 0
        NA = ""
        if B[0] == "1":
            B[1] = "1" + B[1]
            x = 1
        else:
            x = 0
        while x < b:
            c = int(B[x], 10)
            NA += str(int(c/2))
            if x < b-1:
                B[x+1] = str(c%2) + B[x+1]
            x += 1
        return self.power(NA)

if __name__ == '__main__':
    S = Solution()
    B = raw_input()
    A = S.power(B)
    print A
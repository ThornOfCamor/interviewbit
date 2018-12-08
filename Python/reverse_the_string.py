class Solution:
    # @param A : string
    # @return string
    def reverseWords(self, A):
        B = A.split(" ")
        x = 0
        while x < len(B):
            if B[x] == "":
                B.pop(x)
            else:
                x = x + 1
        if len(B) == 1:
            return B[0]
        B.reverse()
        ans = ""
        for x in B:
            ans = ans + " " + x
        return ans[1:len(ans)]

if __name__ == '__main__':
    S = Solution()
    A = S.reverseWords("fwbpudnbrozzifml osdt ulc jsx kxorifrhubk ouhsuhf sswz qfho dqmy sn myq igjgip iwfcqq")
    print A

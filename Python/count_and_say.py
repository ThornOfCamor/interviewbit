class Solution:
    # @param A : integer
    # @return a strings
    def say(self, A):
        if A == "":
            return "1"
        if A == "1":
            return "11"
        B = list(A)
        b = len(B)
        ans  = ""
        c = B[0]
        count = 1
        x = 1
        while x < b:
            if B[x] == B[x-1] and x != b-1:
                count += 1
            elif B[x] == B[x-1]:
                count += 1
                ans += str(count) + c
            elif x == b-1:
                ans += str(count) + c + "1" + str(B[x])
                count = 0
            else:
                ans += str(count) + c
                c = B[x]
                count = 1
            x += 1
        return ans
    
    def countAndSay(self, A):
        if A == 0:
            return ""
        a = ""
        while A > 0:
            a = self.say(a)
            A -= 1
        return a

if __name__ == '__main__':
    S = Solution()
    B = S.countAndSay(4)
    print B

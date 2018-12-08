class Solution:
    # @param A : string
    # @return a list of strings
    def restoreIpAddresses(self, A):
        if len(A) < 4:
            return []
        if len(A) > 12:
            return []
        B = list(A)
        for x in B:
            if x not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                return []
        x = 0
        num1 = []
        if B[0] == '0':
            num1.append('0')
        else:
            num1.append(B[0])
            num1.append(B[0]+B[1])
            if int((B[0]+B[1]+B[2]),10) < 256:
                num1.append(B[0]+B[1]+B[2])
        ans = []
        for a in num1:
            num2 = []
            if len(a) == 1:
                if B[1] == '0':
                    num2.append('0')
                else:
                    num2.append(B[1])
                    num2.append(B[1]+B[2])
                    if int((B[1]+B[2]+B[3]),10) < 256:
                        num2.append(B[1]+B[2]+B[3])
                for b in num2:
                    num3 = []
                    if len(b) == 1:
                        if B[2] == '0':
                            num3.append('0')
                        else:
                            num3.append(B[2])
                            num3.append(B[2]+B[3])
                            if len(B) > 4:
                                if int((B[2]+B[3]+B[4]),10) < 256:
                                    num3.append(B[2]+B[3]+B[4])
                        for c in num3:
                            num4 = []
                            if len(c) == 1:
                                if B[3] == '0':
                                    num4.append('0')
                                else:
                                    num4.append(B[3])
                                    if len(B) > 4:
                                        num4.append(B[3]+B[4])
                                    if len(B) > 5:
                                        if int((B[3]+B[4]+B[5]),10) < 256:
                                            num4.append(B[3]+B[4]+B[5])
                                for d in num4:
                                    if len(a + '.' + b + '.' + c + '.' + d) == len(B) + 3:
                                        ans.append(a + '.' + b + '.' + c + '.' + d)
                            elif len(c) == 2 and len(B)>4:
                                if B[4] == '0':
                                    num4.append('0')
                                else:
                                    num4.append(B[4])
                                    if len(B) > 5:
                                        num4.append(B[4]+B[5])
                                    if len(B) > 6:
                                        if int((B[4]+B[5]+B[6]),10) < 256:
                                            num4.append(B[4]+B[5]+B[6])
                                for d in num4:
                                    if len(a + '.' + b + '.' + c + '.' + d) == len(B) + 3:
                                        ans.append(a + '.' + b + '.' + c + '.' + d)
                            elif len(c) == 3 and len(B)>5:
                                if B[5] == '0':
                                    num4.append('0')
                                else:
                                    num4.append(B[5])
                                    if len(B) > 6:
                                        num4.append(B[5]+B[6])
                                    if len(B) > 7:
                                        if int((B[5]+B[6]+B[7]),10) < 256:
                                            num4.append(B[5]+B[6]+B[7])
                                for d in num4:
                                    if len(a + '.' + b + '.' + c + '.' + d) == len(B) + 3:
                                        ans.append(a + '.' + b + '.' + c + '.' + d)
                    elif len(b) == 2 and len(B)>4:
                        if B[3] == '0':
                            num3.append('0')
                        else:
                            num3.append(B[3])
                            num3.append(B[3]+B[4])
                            if len(B) > 6:
                                if int((B[3]+B[4]+B[5]),10) < 256:
                                    num3.append(B[3]+B[4]+B[5])
                        for c in num3:
                            num4 = []
                            if len(c) == 1:
                                if B[4] == '0':
                                    num4.append('0')
                                else:
                                    num4.append(B[4])
                                    if len(B) > 5:
                                        num4.append(B[4]+B[5])
                                    if len(B) > 6:
                                        if int((B[4]+B[5]+B[6]),10) < 256:
                                            num4.append(B[4]+B[5]+B[6])
                                for d in num4:
                                    if len(a + '.' + b + '.' + c + '.' + d) == len(B) + 3:
                                        ans.append(a + '.' + b + '.' + c + '.' + d)
                            elif len(c) == 2 and len(B)>5:
                                if B[5] == '0':
                                    num4.append('0')
                                else:
                                    num4.append(B[5])
                                    if len(B) > 6:
                                        num4.append(B[5]+B[6])
                                    if len(B) > 7:
                                        if int((B[5]+B[6]+B[7]),10) < 256:
                                            num4.append(B[5]+B[6]+B[7])
                                for d in num4:
                                    if len(a + '.' + b + '.' + c + '.' + d) == len(B) + 3:
                                        ans.append(a + '.' + b + '.' + c + '.' + d)
                            elif len(c) == 3 and len(B)>6:
                                if B[6] == '0':
                                    num4.append('0')
                                else:
                                    num4.append(B[6])
                                    if len(B) > 7:
                                        num4.append(B[6]+B[7])
                                    if len(B) > 8:
                                        if int((B[6]+B[7]+B[8]),10) < 256:
                                            num4.append(B[6]+B[7]+B[8])
                                for d in num4:
                                    if len(a + '.' + b + '.' + c + '.' + d) == len(B) + 3:
                                        ans.append(a + '.' + b + '.' + c + '.' + d)
                    elif len(b) == 3 and len(B)>5:
                        if B[4] == '0':
                            num3.append('0')
                        else:
                            num3.append(B[4])
                            num3.append(B[4]+B[5])
                            if len(B) > 7:
                                if int((B[4]+B[5]+B[6]),10) < 256:
                                    num3.append(B[4]+B[5]+B[6])
                        for c in num3:
                            num4 = []
                            if len(c) == 1:
                                if B[5] == '0':
                                    num4.append('0')
                                else:
                                    num4.append(B[5])
                                    if len(B) > 6:
                                        num4.append(B[5]+B[6])
                                    if len(B) > 7:
                                        if int((B[5]+B[6]+B[7]),10) < 256:
                                            num4.append(B[5]+B[6]+B[7])
                                for d in num4:
                                    if len(a + '.' + b + '.' + c + '.' + d) == len(B) + 3:
                                        ans.append(a + '.' + b + '.' + c + '.' + d)
                            elif len(c) == 2 and len(B)>6:
                                if B[6] == '0':
                                    num4.append('0')
                                else:
                                    num4.append(B[6])
                                    if len(B) > 7:
                                        num4.append(B[6]+B[7])
                                    if len(B) > 8:
                                        if int((B[6]+B[7]+B[8]),10) < 256:
                                            num4.append(B[6]+B[7]+B[8])
                                for d in num4:
                                    if len(a + '.' + b + '.' + c + '.' + d) == len(B) + 3:
                                        ans.append(a + '.' + b + '.' + c + '.' + d)
                            elif len(c) == 3 and len(B)>7:
                                if B[7] == '0':
                                    num4.append('0')
                                else:
                                    num4.append(B[7])
                                    if len(B) > 8:
                                        num4.append(B[7]+B[8])
                                    if len(B) > 9:
                                        if int((B[7]+B[8]+B[9]),10) < 256:
                                            num4.append(B[7]+B[8]+B[9])
                                for d in num4:
                                    if len(a + '.' + b + '.' + c + '.' + d) == len(B) + 3:
                                        ans.append(a + '.' + b + '.' + c + '.' + d)
            elif len(a) == 2 and len(B)>4:
                if B[2] == '0':
                    num2.append('0')
                else:
                    num2.append(B[2])
                    num2.append(B[2]+B[3])
                    if int((B[2]+B[3]+B[4]),10) < 256:
                        num2.append(B[2]+B[3]+B[4])
                for b in num2:
                    num3 = []
                    if len(b) == 1:
                        if B[3] == '0':
                            num3.append('0')
                        else:
                            num3.append(B[3])
                            num3.append(B[3]+B[4])
                            if len(B) > 5:
                                if int((B[3]+B[4]+B[5]),10) < 256:
                                    num3.append(B[3]+B[4]+B[5])
                        for c in num3:
                            num4 = []
                            if len(c) == 1:
                                if B[4] == '0':
                                    num4.append('0')
                                else:
                                    num4.append(B[4])
                                    if len(B) > 5:
                                        num4.append(B[4]+B[5])
                                    if len(B) > 6:
                                        if int((B[4]+B[5]+B[6]),10) < 256:
                                            num4.append(B[4]+B[5]+B[6])
                                for d in num4:
                                    if len(a + '.' + b + '.' + c + '.' + d) == len(B) + 3:
                                        ans.append(a + '.' + b + '.' + c + '.' + d)
                            elif len(c) == 2 and len(B)>5:
                                if B[5] == '0':
                                    num4.append('0')
                                else:
                                    num4.append(B[5])
                                    if len(B) > 6:
                                        num4.append(B[5]+B[6])
                                    if len(B) > 7:
                                        if int((B[5]+B[6]+B[7]),10) < 256:
                                            num4.append(B[5]+B[6]+B[7])
                                for d in num4:
                                    if len(a + '.' + b + '.' + c + '.' + d) == len(B) + 3:
                                        ans.append(a + '.' + b + '.' + c + '.' + d)
                            elif len(c) == 3 and len(B)>6:
                                if B[6] == '0':
                                    num4.append('0')
                                else:
                                    num4.append(B[6])
                                    if len(B) > 7:
                                        num4.append(B[6]+B[7])
                                    if len(B) > 8:
                                        if int((B[6]+B[7]+B[8]),10) < 256:
                                            num4.append(B[6]+B[7]+B[8])
                                for d in num4:
                                    if len(a + '.' + b + '.' + c + '.' + d) == len(B) + 3:
                                        ans.append(a + '.' + b + '.' + c + '.' + d)
                    elif len(b) == 2 and len(B)>5:
                        if B[4] == '0':
                            num3.append('0')
                        else:
                            num3.append(B[4])
                            num3.append(B[4]+B[5])
                            if len(B) > 7:
                                if int((B[4]+B[5]+B[6]),10) < 256:
                                    num3.append(B[4]+B[5]+B[6])
                        for c in num3:
                            num4 = []
                            if len(c) == 1:
                                if B[5] == '0':
                                    num4.append('0')
                                else:
                                    num4.append(B[5])
                                    if len(B) > 6:
                                        num4.append(B[5]+B[6])
                                    if len(B) > 7:
                                        if int((B[5]+B[6]+B[7]),10) < 256:
                                            num4.append(B[5]+B[6]+B[7])
                                for d in num4:
                                    if len(a + '.' + b + '.' + c + '.' + d) == len(B) + 3:
                                        ans.append(a + '.' + b + '.' + c + '.' + d)
                            elif len(c) == 2 and len(B)>6:
                                if B[6] == '0':
                                    num4.append('0')
                                else:
                                    num4.append(B[6])
                                    if len(B) > 7:
                                        num4.append(B[6]+B[7])
                                    if len(B) > 8:
                                        if int((B[6]+B[7]+B[8]),10) < 256:
                                            num4.append(B[6]+B[7]+B[8])
                                for d in num4:
                                    if len(a + '.' + b + '.' + c + '.' + d) == len(B) + 3:
                                        ans.append(a + '.' + b + '.' + c + '.' + d)
                            elif len(c) == 3 and len(B)>7:
                                if B[7] == '0':
                                    num4.append('0')
                                else:
                                    num4.append(B[7])
                                    if len(B) > 8:
                                        num4.append(B[7]+B[8])
                                    if len(B) > 9:
                                        if int((B[7]+B[8]+B[9]),10) < 256:
                                            num4.append(B[7]+B[8]+B[9])
                                for d in num4:
                                    if len(a + '.' + b + '.' + c + '.' + d) == len(B) + 3:
                                        ans.append(a + '.' + b + '.' + c + '.' + d)
                    elif len(b) == 3 and len(B)>6:
                        if B[5] == '0':
                            num3.append('0')
                        else:
                            num3.append(B[5])
                            num3.append(B[5]+B[6])
                            if len(B) > 8:
                                if int((B[5]+B[6]+B[7]),10) < 256:
                                    num3.append(B[5]+B[6]+B[7])
                        for c in num3:
                            num4 = []
                            if len(c) == 1:
                                if B[6] == '0':
                                    num4.append('0')
                                else:
                                    num4.append(B[6])
                                    if len(B) > 7:
                                        num4.append(B[6]+B[7])
                                    if len(B) > 8:
                                        if int((B[6]+B[7]+B[8]),10) < 256:
                                            num4.append(B[6]+B[7]+B[8])
                                for d in num4:
                                    if len(a + '.' + b + '.' + c + '.' + d) == len(B) + 3:
                                        ans.append(a + '.' + b + '.' + c + '.' + d)
                            elif len(c) == 2 and len(B)>7:
                                if B[7] == '0':
                                    num4.append('0')
                                else:
                                    num4.append(B[7])
                                    if len(B) > 8:
                                        num4.append(B[7]+B[8])
                                    if len(B) > 9:
                                        if int((B[7]+B[8]+B[9]),10) < 256:
                                            num4.append(B[7]+B[8]+B[9])
                                for d in num4:
                                    if len(a + '.' + b + '.' + c + '.' + d) == len(B) + 3:
                                        ans.append(a + '.' + b + '.' + c + '.' + d)
                            elif len(c) == 3 and len(B)>8:
                                if B[8] == '0':
                                    num4.append('0')
                                else:
                                    num4.append(B[8])
                                    if len(B) > 9:
                                        num4.append(B[8]+B[9])
                                    if len(B) > 10:
                                        if int((B[8]+B[9]+B[10]),10) < 256:
                                            num4.append(B[8]+B[9]+B[10])
                                for d in num4:
                                    if len(a + '.' + b + '.' + c + '.' + d) == len(B) + 3:
                                        ans.append(a + '.' + b + '.' + c + '.' + d)
            elif len(a) == 3 and len(B)>5:
                if B[3] == '0':
                    num2.append('0')
                else:
                    num2.append(B[3])
                    num2.append(B[3]+B[4])
                    if int((B[3]+B[4]+B[5]),10) < 256:
                        num2.append(B[3]+B[4]+B[5])
                for b in num2:
                    num3 = []
                    if len(b) == 1:
                        if B[4] == '0':
                            num3.append('0')
                        else:
                            num3.append(B[4])
                            num3.append(B[4]+B[5])
                            if len(B) > 6:
                                if int((B[4]+B[5]+B[6]),10) < 256:
                                    num3.append(B[4]+B[5]+B[6])
                        for c in num3:
                            num4 = []
                            if len(c) == 1:
                                if B[5] == '0':
                                    num4.append('0')
                                else:
                                    num4.append(B[5])
                                    if len(B) > 6:
                                        num4.append(B[5]+B[6])
                                    if len(B) > 7:
                                        if int((B[5]+B[6]+B[7]),10) < 256:
                                            num4.append(B[5]+B[6]+B[7])
                                for d in num4:
                                    if len(a + '.' + b + '.' + c + '.' + d) == len(B) + 3:
                                        ans.append(a + '.' + b + '.' + c + '.' + d)
                            elif len(c) == 2 and len(B)>6:
                                if B[6] == '0':
                                    num4.append('0')
                                else:
                                    num4.append(B[6])
                                    if len(B) > 7:
                                        num4.append(B[6]+B[7])
                                    if len(B) > 8:
                                        if int((B[6]+B[7]+B[8]),10) < 256:
                                            num4.append(B[6]+B[7]+B[8])
                                for d in num4:
                                    if len(a + '.' + b + '.' + c + '.' + d) == len(B) + 3:
                                        ans.append(a + '.' + b + '.' + c + '.' + d)
                            elif len(c) == 3 and len(B)>7:
                                if B[7] == '0':
                                    num4.append('0')
                                else:
                                    num4.append(B[7])
                                    if len(B) > 8:
                                        num4.append(B[7]+B[8])
                                    if len(B) > 9:
                                        if int((B[7]+B[8]+B[9]),10) < 256:
                                            num4.append(B[7]+B[8]+B[9])
                                for d in num4:
                                    if len(a + '.' + b + '.' + c + '.' + d) == len(B) + 3:
                                        ans.append(a + '.' + b + '.' + c + '.' + d)
                    elif len(b) == 2 and len(B)>6:
                        if B[5] == '0':
                            num3.append('0')
                        else:
                            num3.append(B[5])
                            num3.append(B[5]+B[6])
                            if len(B) > 8:
                                if int((B[5]+B[6]+B[7]),10) < 256:
                                    num3.append(B[5]+B[6]+B[7])
                        for c in num3:
                            num4 = []
                            if len(c) == 1:
                                if B[6] == '0':
                                    num4.append('0')
                                else:
                                    num4.append(B[6])
                                    if len(B) > 7:
                                        num4.append(B[6]+B[7])
                                    if len(B) > 8:
                                        if int((B[6]+B[7]+B[8]),10) < 256:
                                            num4.append(B[6]+B[7]+B[8])
                                for d in num4:
                                    if len(a + '.' + b + '.' + c + '.' + d) == len(B) + 3:
                                        ans.append(a + '.' + b + '.' + c + '.' + d)
                            elif len(c) == 2 and len(B)>7:
                                if B[7] == '0':
                                    num4.append('0')
                                else:
                                    num4.append(B[7])
                                    if len(B) > 8:
                                        num4.append(B[7]+B[8])
                                    if len(B) > 9:
                                        if int((B[7]+B[8]+B[9]),10) < 256:
                                            num4.append(B[7]+B[8]+B[9])
                                for d in num4:
                                    if len(a + '.' + b + '.' + c + '.' + d) == len(B) + 3:
                                        ans.append(a + '.' + b + '.' + c + '.' + d)
                            elif len(c) == 3 and len(B)>8:
                                if B[8] == '0':
                                    num4.append('0')
                                else:
                                    num4.append(B[8])
                                    if len(B) > 9:
                                        num4.append(B[8]+B[9])
                                    if len(B) > 10:
                                        if int((B[8]+B[9]+B[10]),10) < 256:
                                            num4.append(B[8]+B[9]+B[10])
                                for d in num4:
                                    if len(a + '.' + b + '.' + c + '.' + d) == len(B) + 3:
                                        ans.append(a + '.' + b + '.' + c + '.' + d)
                    elif len(b) == 3 and len(B)>7:
                        if B[6] == '0':
                            num3.append('0')
                        else:
                            num3.append(B[6])
                            num3.append(B[6]+B[7])
                            if len(B) > 9:
                                if int((B[6]+B[7]+B[8]),10) < 256:
                                    num3.append(B[6]+B[7]+B[8])
                        for c in num3:
                            num4 = []
                            if len(c) == 1:
                                if B[7] == '0':
                                    num4.append('0')
                                else:
                                    num4.append(B[7])
                                    if len(B) > 8:
                                        num4.append(B[7]+B[8])
                                    if len(B) > 9:
                                        if int((B[7]+B[8]+B[9]),10) < 256:
                                            num4.append(B[7]+B[8]+B[9])
                                for d in num4:
                                    if len(a + '.' + b + '.' + c + '.' + d) == len(B) + 3:
                                        ans.append(a + '.' + b + '.' + c + '.' + d)
                            elif len(c) == 2 and len(B)>8:
                                if B[8] == '0':
                                    num4.append('0')
                                else:
                                    num4.append(B[8])
                                    if len(B) > 9:
                                        num4.append(B[8]+B[9])
                                    if len(B) > 10:
                                        if int((B[8]+B[9]+B[10]),10) < 256:
                                            num4.append(B[8]+B[9]+B[10])
                                for d in num4:
                                    if len(a + '.' + b + '.' + c + '.' + d) == len(B) + 3:
                                        ans.append(a + '.' + b + '.' + c + '.' + d)
                            elif len(c) == 3 and len(B)>9:
                                if B[9] == '0':
                                    num4.append('0')
                                else:
                                    num4.append(B[9])
                                    if len(B) > 10:
                                        num4.append(B[9]+B[10])
                                    if len(B) > 11:
                                        if int((B[9]+B[10]+B[11]),10) < 256:
                                            num4.append(B[9]+B[10]+B[11])
                                for d in num4:
                                    if len(a + '.' + b + '.' + c + '.' + d) == len(B) + 3:
                                        ans.append(a + '.' + b + '.' + c + '.' + d)
        ans.sort()
        return ans

if __name__ == '__main__':
    S = Solution()    
    A = S.restoreIpAddresses("123123123")
    print A

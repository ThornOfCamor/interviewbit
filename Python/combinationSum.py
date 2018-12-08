class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    
    def combinationSum(self, A, B):
        if len(A)==0:
            return []
        if len(A)==1 and B%A[0] != 0:
            return []
        if B < min(A):
            return []
        C = self.combinations([], A, B)
        C.sort()
        return C

    def combinations(self, currList, A, B):
        C = []
        D = []
        if len(A) == 0 or B == 0:
            return []
        if B < min(A):
            return []
        currListnew1 = []
        currListnew2 = []
        for x in currList:
            currListnew1.append(x)
            currListnew2.append(x)
        flag = 0
        for x in A:
            if x == B:
                if flag == 0:
                    currListnew1.append(x)
                if currListnew1 not in C:
                    C.append(currListnew1)
                    flag = 1
            else :
                D.append(x)
        if len(D) == 0:
            return C
        d = max(D)
        if d < B :
            currListnew2.append(d)
            C.extend(self.combinations(currListnew2, D, B-d))
        while d in D:
            D.pop(D.index(d))
        C.extend(self.combinations(currList, D, B))
        return C

if __name__ == '__main__':
    A = [1, 2]
    B = 2
    S = Solution()
    C = S.combinationSum(A, B)
    print C
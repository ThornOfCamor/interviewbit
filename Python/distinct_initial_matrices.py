from math import factorial, sqrt
class Solution:
    # @param A : list of integers
    # @return an integer
    def __init__(self):
        self.n = 0

    def isPrime(self, n):
        if n < 2:
            return 0
        if n <= 3:
            return 1
        if n%2==0 or n%3==0: 
            return 0
        i = 5
        while i*i <= n:
            if n%i==0 or n%(i+2)==0:
                return 0
            i += 6
        return 1

    def HCF(self, A, B):
        if A > B:
            self.coPrime(B, A)
        if A%B == 0:
            return B
        self.coPrime(B, A%B)
    
    def S(self, A):
        return (factorial(A)**(self.n/A))%1000000007

    def factors(self, A):
        if A == 1:
            return [1]
        if self.isPrime(A):
            return [1, A]
        x = 2
        ans = [1, A]
        while x*x < A:
            if A%x == 0:
                ans.append(x)
                ans.append(A/x)
            x += 1
        if x*x == A:
            ans.append(x)
        ans.sort()
        return ans
    
    def cntMatrix(self, A):
        interval = [1]
        self.n = len(A)
        if self.n == 0:
            return 0
        if self.n == 1:
            return 1
        x = 1
        curr = 0
        while x < self.n:
            if A[x] < A[x-1]:
                curr += 1
                interval.append(1)
            else:
                interval[curr] += 1
            x += 1
        maxi = max(interval)
        if maxi == 1:
            return 1
        for x in interval:
            for y in interval:
                if self.HCF(x, y) == 1:
                    return 1
        ans = 0
        C = self.factors(min(interval))
        for x in C:
            ans += self.S(x)
        return ans%1000000007

if __name__ == '__main__':
    S = Solution()
    A = [1, 3, 4, 24]
    C = S.cntMatrix(A)
    print C

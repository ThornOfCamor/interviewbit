"""
Permutations
"""

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def rotate(self, B, n):
    	A = []
    	for x in range(len(B)):
    		A.append(B[x])
        if n == 0:
            return A
        i = 1
        temp1 = A[0]
        A[0] = A[len(A)-1]
        while i < len(A):
            temp2 = A[i]
            A[i] = temp1
            temp1 = temp2
            i = i + 1
        return self.rotate(A, n-1)
        
    def switch(self, B, i, j):
        A = []
    	for x in range(len(B)):
    		A.append(B[x])
        temp = A[i]
        A[i] = A[j]
        A[j] = temp
        return A
    
    def permute(self, A):
    	D = A
        B = []
        if A == [] or  len(A)==1:
            B.append(A)
            return B
        B.append(A)
        C = []
        i = 1
        while i< len(A):
            C = A
            C = self.rotate(C, i)
            if C not in B:
            	B.append(C)
            i = i + 1
        j = 0
        while j < len(A)-1:
            k = j + 1
            while k < len(A):
                C = self.switch(A, j, k)
                if C not in B:
                    B.append(C)
                    i = 1
                    while i < len(A):
                        C = self.rotate(C, i)
                        if C not in B:
                            B.append(C)
                        i = i + 1
                k = k + 1
            j = j + 1
        return B


if __name__ == '__main__':
	A = list(range(15))
	B = []
	C = Solution()
	B = C.permute(A)
	print B

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    
    def bin_search(self, A, B, low, high):
        if B < A[low]:
            return low
        if B > A[high]:
            return high + 1
        if low==high:
            if A[low] == B:
                return low
            else:
                return low + 1
        mid = int((low+high)/2)
        if B == A[mid]:
            return mid
        if B < A[mid]:
            return self.bin_search(A, B, low, mid-1)
        return self.bin_search(A, B, mid+1, high)
    
    def searchInsert(self, A, B):
        if B <= A[0]:
            return 0
        elif B > A[len(A)-1]:
            return len(A)
        elif B == A[len(A)-1]:
            return len(A) - 1
        
        return self.bin_search(A, B, 0, len(A)-1)

if __name__ == '__main__':
    S = Solution()
    A = S.searchInsert([1,3,5,7], 2)
    print A    

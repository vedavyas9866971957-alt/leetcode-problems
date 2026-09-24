class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def sum_digits(n):
            s=0
            while(n!=0):
                d=n%10
                s+=d
                n//=10
            return s
        for i,val in enumerate(nums):
            
            if i==sum_digits(val):
                return i
        return -1
                
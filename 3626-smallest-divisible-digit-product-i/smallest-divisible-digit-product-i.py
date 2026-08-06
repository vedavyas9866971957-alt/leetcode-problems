class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        
        def productofdigits(n):
            p=1
            while(n!=0):
                d=n%10
                p*=d
                n//=10
            return p

        i=n
        while(productofdigits(i)%t!=0):
            i+=1
        return i
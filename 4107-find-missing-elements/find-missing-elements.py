class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        min=float("inf")
        max=-min
        for num in nums:
            if num>max:
                max=num
            if num<min:
                min=num
        setnums=set(nums)
        res=[]
        for i in range(min,max+1):
            if i not in setnums:
                res.append(i)
        return res
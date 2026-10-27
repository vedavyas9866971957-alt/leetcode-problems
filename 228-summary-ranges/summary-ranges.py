class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if len(nums)==0:
            return []
        start=nums[0]
        prev=start
        res=[]
        for i in range(1,len(nums)):
            if nums[i]==prev+1:
                prev=nums[i]
                continue
            if start-prev==0:
                res.append(str(start))
                
            else:
                res.append(f"{start}->{prev}")
            start=nums[i]
            prev=start
        if start-prev==0:
            res.append(str(start))
                
        else:
            res.append(f"{start}->{prev}")
            
        return res
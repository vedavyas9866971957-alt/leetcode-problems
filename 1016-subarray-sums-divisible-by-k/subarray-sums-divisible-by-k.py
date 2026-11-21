class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        prefix={0:1}
        tot=0
        count=0
        for num in nums:
            tot+=num
            tot%=k
            print (tot)
            if tot in prefix:
                count+=prefix[tot]
            prefix[tot]=prefix.get(tot,0)+1
        return count
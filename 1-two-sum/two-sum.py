class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        search={}
        for i in range(len(nums)):
            num=nums[i]
            diff=target-num
            if diff in search:
                return [search[diff],i]
            search[num]=i
        
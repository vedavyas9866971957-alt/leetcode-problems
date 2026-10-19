class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        freq_target=0
        noof_min_elements=0
        for num in nums:
            if num==target:
                freq_target+=1
            if num<target:
                noof_min_elements+=1
        return list(range(noof_min_elements,noof_min_elements+freq_target))
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        hashmap={}
        for i,val in enumerate(numbers,1):
            if target-val in hashmap:
                return [hashmap[target-val],i]
            hashmap[val]=i
        
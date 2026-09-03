class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        m=float("inf")
        odd=False
        for n in nums1:
            if n%2==1:
                odd=True
            m=n if n<m else m
        return (m%2==1 and odd) or not odd
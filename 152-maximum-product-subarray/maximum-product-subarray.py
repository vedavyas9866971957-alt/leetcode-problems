class Solution:
   def maxProduct(self, nums: List[int]) -> int:
       max_prod = -11
       prod1, prod2 = 1, 1
       size = len(nums)

       for i in range(0, size):
           j = size - i - 1
           prod1 *= nums[i]
           max_prod = max(prod1, max_prod)
           if prod1 == 0:
               prod1 = 1
           prod2 *= nums[j]
           max_prod = max(prod2, max_prod)
           if prod2 == 0:
               prod2 = 1
       return max_prod
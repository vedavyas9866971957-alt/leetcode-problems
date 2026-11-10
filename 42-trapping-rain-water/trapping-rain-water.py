class Solution:
    def trap(self, height: list[int]) -> int:
        leftmax=0
        rightmax=0
        left=0
        right=len(height)-1
        ans=0
        while(left<=right):
            if rightmax>leftmax:
                leftmax=max(leftmax,height[left])
                ans+=leftmax-height[left]
                left+=1
            else:
                rightmax=max(rightmax,height[right])
                ans+=rightmax-height[right]
                right-=1
        return ans
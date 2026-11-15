class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
            q=deque()
            res=[]
            for i,val in enumerate(nums):
                while(q and val>nums[q[-1]]):#=
                    q.pop()
                q.append(i)
                
                if q[0]<=i-k:
                    q.popleft()
                if i>=k-1:
                    res.append(nums[q[0]])
                    
            return res

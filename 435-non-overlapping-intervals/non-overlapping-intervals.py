class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        count=0
        
        prev=0
        for i in range(1,len(intervals)):
            if intervals[i][0]<intervals[prev][1]:
                count+=1
                if intervals[i][1]<intervals[prev][1]:
                    prev=i
                
            else:
                prev=i
        return count
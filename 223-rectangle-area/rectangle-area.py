class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        #calculate intersection area
        hight=min(by2,ay2)-max(by1,ay1)
        width=min(ax2,bx2)-max(ax1,bx1)
        intersect=max(0,width)*max(0,hight)
        #calculate individual areas
        a=abs(ax1-ax2)*abs(ay1-ay2)
        b=abs(bx1-bx2)*abs(by1-by2)
        return a+b-intersect
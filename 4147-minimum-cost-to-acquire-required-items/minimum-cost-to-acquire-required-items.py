class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        totalcost=0
        if costBoth<cost1+cost2:
            if need1<need2:
                totalcost+=need1*costBoth
                need2-=need1
                need1=0
                
            else:
                totalcost+=need2*costBoth
                need1-=need2
                need2=0
        
        totalcost+=need1*min(cost1,costBoth)
        totalcost+=need2*min(cost2,costBoth)
        return totalcost

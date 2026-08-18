class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        if rowIndex==0:
            return [1]
        if  rowIndex==1:
            return [1,1]
        curr=[1,1]
        for i in range(rowIndex-1):
            new=[1]
            for j in range(len(curr)-1):
                new.append(curr[j]+curr[j+1])
            new.append(1)
            curr=new
        return curr

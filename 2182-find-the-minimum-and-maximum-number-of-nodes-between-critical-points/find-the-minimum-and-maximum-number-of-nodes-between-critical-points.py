# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if  head.next.next==None:
            return [-1,-1] 
        start=0
        prev=head
        curr=head.next
        nex=head.next.next
        mindis=99999
        maxdis=-1
        ind=0
        crits=[-1,-1]
        while(nex):
            if prev.val<curr.val>nex.val or prev.val>curr.val<nex.val:
                if crits[0]==-1:
                    crits[0]=ind
                else:
                    crits[1]=ind
                if crits[1]==-1:
                    start=ind
                if crits[1]!=-1 and crits[1]-crits[0]<mindis:
                    mindis=crits[1]-crits[0]
                if crits[1]!=-1:
                    crits[0]=crits[1] 
            ind+=1
            prev=curr
            curr=nex
            nex=nex.next
        if crits[1]==-1:
            return [-1,-1]
        maxdis=crits[-1]-start
        print(start,crits[-1])
        
        return [mindis,maxdis]

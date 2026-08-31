# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if  head.next.next==None:
            return [-1,-1] 
        
        prev=head
        curr=head.next
        nex=head.next.next
        mindis=99999
        maxdis=-1
        ind=0
        crits=[]
        while(nex):
            if prev.val<curr.val>nex.val or prev.val>curr.val<nex.val:
                crits.append(ind)
                if len(crits)>=2 and crits[-1]-crits[-2]<mindis:
                    mindis=crits[-1]-crits[-2]
            ind+=1
            prev=curr
            curr=nex
            nex=nex.next
        if len(crits)<2:
            return [-1,-1]
        maxdis=crits[-1]-crits[0]
        return [mindis,maxdis]

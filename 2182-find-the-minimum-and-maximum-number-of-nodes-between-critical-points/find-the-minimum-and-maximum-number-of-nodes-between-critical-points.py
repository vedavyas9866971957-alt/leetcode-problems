class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        if head is None or head.next is None or head.next.next is None:
            return [-1, -1]

        prev = head
        curr = head.next
        nex = curr.next

        first = -1
        last = -1
        min_dist = float('inf')

        index = 1

        while nex:
            if (curr.val > prev.val and curr.val > nex.val) or \
               (curr.val < prev.val and curr.val < nex.val):

                if first == -1:
                    first = index
                else:
                    min_dist = min(min_dist, index - last)

                last = index

            prev = curr
            curr = nex
            nex = nex.next
            index += 1

        if first == -1 or first == last:
            return [-1, -1]

        max_dist = last - first

        return [min_dist, max_dist]
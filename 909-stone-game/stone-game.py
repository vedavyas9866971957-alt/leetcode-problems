class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @cache
        def best(left,right):
            if left==right:
                return piles[left]

            #choosing left
            leftchoose=piles[left]-best(left+1,right)
            rightchoose=piles[right]-best(left,right-1)
            return max(leftchoose,rightchoose)
        return best(0,len(piles)-1)>0
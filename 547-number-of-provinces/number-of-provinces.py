class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited=[0]*len(isConnected)
        start=0
        ans=0
        def dfs(start):
            visited[start]=1
            for i,neigh in enumerate(isConnected[start]):
                if neigh==1 and not visited[i]:
                    dfs(i)
        for i in range(len(visited)):
            if not visited[i]:
                dfs(i)
                ans+=1
        return ans

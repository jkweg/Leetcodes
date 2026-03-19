class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        visited = [False] * n
            
        def DFSvisit(isConnected,v):
            visited[v] = True
            for u in range(n):
                if isConnected[v][u] == 1 and not visited[u]:
                    DFSvisit(isConnected,u)
        cnt = 0 
        for i in range(n):
            if not visited[i]:
                DFSvisit(isConnected,i)
                cnt +=1

        return cnt

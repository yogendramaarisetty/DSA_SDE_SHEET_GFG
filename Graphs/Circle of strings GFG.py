class Graph:
        def __init__(self):
            self.data = {}
            self.indegree = {}
            
        def addEdge(self,n1,n2):
            if n1 in self.data:
                self.data[n1].append(n2)
            else:
                self.data[n1] = [n2]
            
            if n2 in self.indegree:
                self.indegree[n2]+=1
            else:
                self.indegree[n2]=1
        
        def dfsUtil(self,curr,visited):
            if curr not in visited:
                return
            visited[curr] = True
            for neighbor in self.data[curr]:
                if neighbor not in visited:
                    return
                if not visited[neighbor]:
                    self.dfsUtil(neighbor,visited)
        
        def getTranspose(self):
            self.indegree = {}
            transposedData = {}
            for k in self.data:
                for neighbor in self.data[k]:
                    #for adding edge
                    if neighbor in transposedData:
                        transposedData[neighbor].append(k)
                    else:
                        transposedData[neighbor] = [k]
                    
                    #for indegree
                    if k in self.indegree:
                        self.indegree[k]+=1
                    else:
                        self.indegree[k]=1
            return transposedData
                    
        #also called eulerian - using kosaraju algorithm
        def isStronglyConnected(self):
            visited = {}
            
            for k in self.data:
                visited[k] = False
                
            for k in self.data:
                curr = k
                break
            
            self.dfsUtil(curr,visited)
            
            for v in visited:
                if not visited[v]:
                    return False
            transData = self.getTranspose()
            if len(self.data) !=  len(transData):
                return False
            self.data = transData
            visited = {}
            
            for k in self.data:
                visited[k] = False

            self.dfsUtil(curr,visited)
            
            for v in visited:
                if not visited[v]:
                    return False
            return True
        
        def isEulerianCycle(self):
            if not self.isStronglyConnected():
                return False
            
            for i in self.indegree:
                if len(self.data[i]) != self.indegree[i]:
                    return False
            return True
class Solution:
    def isCircle(self, N, A):
        graph = Graph()
        for s in A:
            graph.addEdge(s[0],s[-1])
        
        return 1 if graph.isEulerianCycle() else 0
import sys
sys.setrecursionlimit(10**6)
if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        
        N = int(input())
        A = input().split()
        
        ob = Solution()
        print(ob.isCircle(N, A))
from queue import Queue
class Graph:

    def __init__(self,num_nodes,edges,weighted=False,directed=False):
        self.weighted = weighted
        self.directed = directed
        self.num_nodes = num_nodes
        self.data = [[] for i in range(num_nodes)]
        for edge in edges:
            if self.weighted:
                n1,n2,w = edge
                self.data[n1].append((n2,w))
                if not self.directed:
                    self.data[n2].append((n1,w))
            else:
                n1,n2 = edge
                self.data[n1].append(n2)
                if not self.directed:
                    self.data[n2].append(n1)


    def add_edge(self,edge):
        n1,n2 = edge
        self.data[n1].append(n2)
        self.data[n2].append(n1)
    
    def __repr__(self):
        return str("\n".join([f'{i} -> {d}' for i,d in enumerate(self.data)]))

    def dfs(self,start,goal = None):
        if goal != None:
            print('src:',start,'','dest:',goal)
        else:
            print(f'Traversal from {start}')
        s = [start]
        distance = [0 for i in range(self.num_nodes)]
        parent = {start: None}
        while len(s)!=0:
            print(s)
            curr = s.pop()
            print(curr,end=' ')
            if goal != None and curr == goal:
                r = self.get_path(parent,start,goal)
                return 
            for neighbor in self.data[curr]:
                if neighbor not in parent:
                    s.append(neighbor)
                    parent[neighbor] = curr
                    distance[neighbor] = 1+ distance[curr]
        print('distance:',distance,'parent:',parent)
    
    def dfs_recursive(self,start,goal,pred):
        print(start,end='-> ')
        if start == goal:
            print('Found element:',pred)
            return pred
        
        for neighbor in self.data[start]:
            if neighbor not in pred:
                pred[neighbor] = start
                self.dfs_recursive(neighbor,goal,pred)
        return pred
    #We are not searching but traversing for now
    def bfs(self,start, goal= None):
        if goal != None:
            print('src:',start,'','dest:',goal)
        else:
            print(f'Traversal from {start}')
        q = Queue(self.num_nodes)
        distance = [0 for i in range(self.num_nodes)]
        q.put(start)
        pred = {start:None}
        while not q.empty():
            curr = q.get()
            print(curr,end=' ')
            if goal is not None and curr == goal:
                r = self.get_path(pred,start,goal)
                return
            for neighbor in self.data[curr]:
                if neighbor not in pred:
                    distance[neighbor] = distance[curr]+1
                    q.put(neighbor)
                    pred[neighbor] = curr

    
    def get_path(self,pred,start,goal):
        r = [goal]
        p = pred[goal]
        while p != start:
            r.append(p)
            p = pred[p]
        r.append(start)
        return "->".join([str(i) for i in r[::-1]])



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


def get_path(pred,start,goal):
    r = [goal]
    p = pred[goal]
    while p is not None and p != start:
        r.append(p)
        p = pred[p]
    r.append(start)
    return "->".join([str(i) for i in r[::-1]])




if __name__ == '__main__':
    edges = [(0,1),(4,3),(0,4),(1,2),(1,3),(1,4),(3,2)]
    g1 = Graph(5,edges)
    #print(g1)
    #g1.add_edge((0,3))
    #print(g1)
    # for i in range(5):
    #     g1.bfs(i)
    #     print()
    print(g1)
    # print("BFS results")
    # g1.bfs(0)
    # print()
    # g1.bfs(0,2)
    # print()
    # g1.bfs(4,2)

    # print("\n\n==========================\n\nDFS results")
    # g1.dfs(0)
    # print()
    # g1.dfs(0,2)
    # print()
    # g1.dfs(4,2)

    #print("\n\n==========================\n\nDFS Recursive results")
    # print(get_path(g1.dfs_recursive(0,2,{0:None}),0,2))
    # print()
    # path_pred = g1.dfs_recursive(4,2,{4:None})
    # print('Final:',path_pred)
    # print(get_path(path_pred,4,2))
    # Unweighted Directed

    print("Unweighted Directed")
    g3 = Graph(5,edges,directed=True)
    print(g3)

    # Weighted Undirected
    print("Weighted Undirected")
    weighted_edges = [(0,1,3),(0,3,2),(0,8,4),(1,7,4),(2,7,2),(2,3,6),(2,5,1),(3,4,1),(4,8,8),(5,6,8)]
    g2 = Graph(9,weighted_edges,weighted=True)
    print(g2)

    print("Weighted directed")
    # Weighted directed
    g3 = Graph(9,weighted_edges,weighted=True,directed=True)
    print(g3)
    
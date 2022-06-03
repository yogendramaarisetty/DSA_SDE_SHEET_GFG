from queue import Queue
class Graph:
    def __init__(self,num_nodes):
        self.num_nodes = num_nodes
        self.data = [[] for i in range(num_nodes)]

    def __init__(self,num_nodes,edges):
        self.num_nodes = num_nodes
        self.data = [[] for i in range(num_nodes)]
        for n1,n2 in edges:
            self.data[n1].append(n2)
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
                print()
                print(r)
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
                print()
                print(r)
                return
            for neighbor in self.data[curr]:
                if neighbor not in pred:
                    distance[neighbor] = distance[curr]+1
                    q.put(neighbor)
                    pred[neighbor] = curr
        print()
        print(pred)
        print(distance)

    
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
    g1.add_edge((0,3))
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

    print("\n\n==========================\n\nDFS Recursive results")
    # print(get_path(g1.dfs_recursive(0,2,{0:None}),0,2))
    # print()
    path_pred = g1.dfs_recursive(4,2,{4:None})
    print('Final:',path_pred)
    print(get_path(path_pred,4,2))

from tkinter import N
from graph import Graph
from helper import *
from queue import Queue

def dijkstras(graph,src,dst):
    distance = [(100000)-1 for _ in range(graph.num_nodes)]
    distance[src] = 0
    q = Queue(graph.num_nodes)
    unvisited = set([_ for _ in range(graph.num_nodes)])
    
    pred = {src:None}
    q.put(src)
    while not q.empty():
        curr = q.get()
        if curr in unvisited:
            unvisited.remove(curr)
        print(curr,' ->:::')
        print(distance)
        print(unvisited)
        print(pred)
        print()
        min,min_node = 100000,graph.num_nodes+1
        for neighbor,weight in graph.data[curr]:
            if neighbor in unvisited:
                if distance[neighbor]>weight+distance[curr]:
                    distance[neighbor] = weight+distance[curr]
                    pred[neighbor] = curr
                if distance[neighbor]<min:
                    min = distance[neighbor]
                    min_node = neighbor
        if min_node<graph.num_nodes:
            q.put(min_node)
    print(f'######@@@ cost for {src} to {dst}:',distance[dst],'| path:',get_path(pred,src,dst),'***')
        

if __name__ == '__main__':
    #weighted_edges = [(0,1,3),(0,3,2),(0,8,4),(1,7,4),(2,7,2),(2,3,6),(2,5,1),(3,4,1),(4,8,8),(5,6,8)]
    weighted_edges = [(1,2,2),(1,3,4),(2,4,7),(2,3,1),(3,5,3),(4,6,1),(5,4,2),(5,6,5)]
    # g2 = Graph(7,weighted_edges,weighted=True,directed=True)
    g2 = Graph(4,[(0,1,9),(0,2,1),(0,3,1),(1,3,3),(2,3,2)],weighted=True)
    dijkstras(g2,0,3)
    print("/n===========================/n")
    # dijkstras(g2,0,6)
    # print("/n===========================/n")
    # dijkstras(g2,5,6)
    # print("/n===========================/n")
    # dijkstras(g2,2,6)
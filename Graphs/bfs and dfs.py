from graph import Graph
from helper import *





if __name__ == '__main__':
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
    
    g2 = Graph(9,weighted_edges,weighted=True)
    print(g2)

    print("Weighted directed")
    # Weighted directed
    g3 = Graph(9,weighted_edges,weighted=True,directed=True)
    print(g3)
    
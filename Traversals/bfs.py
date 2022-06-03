from helpers import *
from queue_ll import Queue


def bfs(maze,start,goal):
    #if input is given in form of ' ' and '*' 
    if maze[start[0]][start[1]] == '*' or maze[goal[0]][goal[1]] == '*':
        return None
    queue = Queue()
    queue.enqueue(start)
    predecessor = {start:None}
    while not queue.is_empty():
        curr = queue.dequeue()
        if curr == goal:
            print(predecessor)
            return get_path(predecessor,start,goal)
        for dir in ['up','right','down','left']:
            row,col = offsets[dir]
            neighbor = (curr[0]+row , curr[1]+col)
            if is_valid_pos(maze,neighbor) and not neighbor in predecessor:
                queue.enqueue(neighbor)
                predecessor[neighbor] = curr
    return None

if __name__ == "__main__":
    maze = [[0]*3 for i in range(3)]
    #test1
    # path = bfs(maze,(0,0),(2,2))
    # path.reverse()
    # print(path)
    # path = bfs(maze,(0,0),(0,2))
    # path.reverse()
    # print(path)

    #test2
    path = bfs(maze_with_blocks,(0,0),(3,3))
    path.reverse()
    print(path)

    path = bfs(maze_with_blocks,(0,0),(1,3))
    if path is not None:
        path.reverse()
    print(path)
    path = bfs(maze_with_blocks,(0,0),(0,3))
    if path is not None:
        path.reverse()
    print(path)

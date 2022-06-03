from priority_queue import PriorityQueue
from helpers import *
from queue

def heuristic(a,b) -> int:
    return int(abs(a[0]-b[0])+abs(a[1]-b[1]))

def a_star(maze,start,goal):
    pq = PriorityQueue()
    pq.put(start,0)
    g_values = {start : 0}
    predecessor = {start : None}

    while not pq.is_empty():
        curr = pq.get()
        if curr == goal:
            return get_path(predecessor,start,goal)
        for direction in ['up','right','down','left']:
            row, col = offsets[direction]
            neighbor = (curr[0]+row, curr[1]+col)
            if neighbor not in g_values and is_valid_pos(maze,neighbor):
                g_values[neighbor] = g_values[curr]+1
                f_val = g_values[neighbor] + heuristic(neighbor,goal)
                pq.put(neighbor,f_val)
                predecessor[neighbor] = curr
    return None

if __name__ == '__main__':
    path = a_star(maze_with_blocks,(0,0),(3,3))
    if path is not None:
        path.reverse()
    print(path)
        
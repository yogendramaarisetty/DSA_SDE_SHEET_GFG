from stack import Stack
from helpers import *


def dfs(maze,start,goal):
    stack = Stack()
    stack.push(start)
    predecessor = {start:None}
    while not stack.is_empty():
        curr = stack.pop()
        if curr == goal:
            #print(predecessor)
            return get_path(predecessor,start,goal)
        for direction in ["up","right","down","left"]:
            row,col = offsets[direction]
            neighbor = (curr[0]+row, curr[1]+col)
            if is_valid_pos(maze,neighbor) and not neighbor in predecessor:
                stack.push(neighbor)
                predecessor[neighbor] = curr
    return None
            



if __name__ == '__main__':
    maze = [[0] * 3 for i in range(3)]
    path = dfs(maze,(0,0),(2,2))
    path.reverse()
    print(path)
    path = dfs(maze,(0,0),(0,2))
    path.reverse()
    print(path)
    

"""
Pseudo code
------------

DS:
    stack: [start]
    predecessor: {start: None}

Algorithm:
    1. Pop stack
    2. If popped element is equal to goal then return path
    3. Otherwise visit the unvisited neighbors and push them to stack and update predecesor dictionary
    4. Repeat until stack is empty

Visualization
-------------
[(0,0),   (0,1),   (0,2)]
    |
[(1,0),   (1,1),   (1,2)]
    |
[(2,0),--> (2,1), --> (2,2)]

"""
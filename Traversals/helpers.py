maze_with_blocks = [[' ',' ','*',' '],
                    [' ',' ',' ',' '],
                    [' ','*',' ','*'],
                    [' ',' ',' ',' ']]

offsets = {
    "up" : (-1,0),
    "down":(1,0),
    "right":(0,1),
    "left":(0,-1)
}

def get_path(predecessor,start,goal):
    l = [goal]
    i = goal
    while not i == start:
        l.append(predecessor[i])
        i = predecessor[i]
    return l

def is_valid_pos(maze,neighbor):
    #if input is given in form of ' ' and '*' 

    return neighbor[0] in range(0,len(maze)) and neighbor[1] in range(0, len(maze[0])) and not maze[neighbor[0]][neighbor[1]] == '*' 

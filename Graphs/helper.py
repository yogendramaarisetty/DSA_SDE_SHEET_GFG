

def get_path(pred,start,goal):
    r = [goal]
    if goal not in pred:
        return "No Path found"
    p = pred[goal]
    while p is not None and p != start:
        r.append(p)
        if p not in pred:
            return "No Path found"
        p = pred[p]
    r.append(start)
    return "->".join([str(i) for i in r[::-1]])

edges = [(0,1),(4,3),(0,4),(1,2),(1,3),(1,4),(3,2)]
weighted_edges = [(0,1,3),(0,3,2),(0,8,4),(1,7,4),(2,7,2),(2,3,6),(2,5,1),(3,4,1),(4,8,8),(5,6,8)]
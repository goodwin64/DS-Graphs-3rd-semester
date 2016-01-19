from Lec8_Graph import Graph, Vertex
from Lec8_Queue import Queue
from lab1 import readFromAdjacencyMatrix

def prettyDict(d):
    for key in d:
        print("{0} -> {1}".format(key, d[key]))


def bfs_paths(graph, start, goal):
    '''Breadth-First Search Algorithm'''
    res = []
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                res.append(path + [next])
            else:
                queue.append((next, path + [next]))
    return res


def shortest_path(graph, start, goal):
    lists = bfs_paths(graph, start, goal)
    minLen = len(min(lists, key=len))
    return list(filter(lambda lis: len(lis) == minLen, lists))
             

def bfs(g,start):
    '''Breadth-First Search Algorithm'''
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.insert(start)
    while (vertQueue.size() > 0):
        currentVert = vertQueue.remove()
        for nbr in currentVert.getConnections():
            if (nbr.getColor() == 'white'):
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.insert(nbr)
        currentVert.setColor('black')


def traverse(y):
    
    x = y
    while (x.getPred()):
        print(x.getId())
        x = x.getPred()
    print(x.getId())


g = {}
G, M = readFromAdjacencyMatrix()

for v in G:
    for w in v.getConnections():
        if v.getId() in g:
            g[v.getId()].add(w.getId())
        else:
            g[v.getId()] = set([w.getId()])

print(shortest_path(g, 1, 6))


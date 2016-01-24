__author__ = "Max Donchenko (https://github.com/goodwin64)"

graph = {'A': set(['B', 'C', 'D']),
         'B': set(['A', 'D']),
         'C': set(['A', 'G']),
         'D': set(['A', 'B', 'F']),
         'F': set(['D', 'G', 'H']),
         'G': set(['C', 'F', 'H']),
         'H': set(['F', 'G'])}

def prettyPrint(M):
    for row in M:
        print(row)

def dfs_paths(graph, start, goal):
    '''depth-first search algorithm'''
    res = []
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                res.append( path + [next] )
            else:
                stack.append((next, path + [next]))
    return res

def minL(*lists):
    '''return the list of the lists with the shortest lengths'''
    res = []
    minLen = len(min(lists[0]))
    for ls in lists[0]:
        if len(ls) == minLen:
            res.append(ls)
    return res

L = list( dfs_paths(graph, 'B', 'G') )
prettyPrint( minL( L ) )

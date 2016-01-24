from Lec8_Graph import Vertex, Graph

def prettyPrint(M):
    for row in M:
        print(row)

def countEdges(M):
    edges = 0
    for i in range(len(M)):
        for j in range(i+1):
            if M[i][j] == 1:
                edges += 1
    return edges

def readline(file):
    '''In case when first line contains <string>-info about matrix'''
    char = file.read(1)
    chars = [char]
    while char != '\n':
        char = file.read(1)
        chars.append(char)
        
    return str().join(chars[:-1])
    

def readFromAdjacencyMatrix(G=Graph()):
    Matrix = []
    f = open('m1.txt', 'r')

    # line-by-line reading from file and casting to <integer> type
    for line in f:
        Matrix.append( list( map( int, line.split())) )

    for row in range(1, len(Matrix)+1):
        for cell in range(1, len(Matrix)+1):
            if Matrix[row-1][cell-1] != 0:
                G.addEdge(row, cell)

    f.close()
    return G, Matrix

def writeToIncidenceMatrix(G, M1):
    '''M1 - adjacency matrix which we read from the file
       M2 - incidence matrix which we create and write to a new file
    '''
    edges = countEdges(M1)
    M2 = [[0 for i in range(edges)] for j in range(len(G.vertList))]
                
    f = open('m2.txt', 'w')
    c = 0
    for i in range(len(M1)):
        for j in range(i+1):
            if M1[i][j] == 1:
                M2[i][c] = 1
                M2[j][c] = 1
                c += 1

    chr0 = 65
    f.write(" ")
    for cell in range(1, len(M2[0])+1):
        f.write("{0:3d}".format(cell))
    f.write("\n")
    for cell in range(1, len(M2[0])*3):
        f.write("_")
    f.write("\n")
    for row in M2:
        f.write("{0}".format(chr(chr0)))
        chr0 += 1
        for cell in row:
            f.write("{0:3d}".format(cell))
        f.write("\n")

    f.close()
    return M2

def writeToDistanceMatrix(G, M1):
    '''M1 - adjacency matrix which we read from the file
       M3 - distance matrix which we create and write to a new file
    '''
    INF = 99 # some big number as kind of infinity
    M3 = [[row[i] for i in range(len(M1))] for row in M1] # M3 is copy of M1

    # Cells with 0-value except diagonal are init by infinity or big number
    for i in range(len(M3)):
        for j in range(len(M3)):
            if M3[i][j] == 0:
                M3[i][j] = INF

    # Initializing diagonal with zeros
    for i in range(len(M3)):
        for j in range(len(M3)):
            if i == j:
                M3[i][j] = 0

    # Floyd–Warshall algorithm
    for k in range(len(M3)):
        for i in range(len(M3)):
            for j in range(len(M3)):
                M3[i][j] = min(M3[i][j], M3[i][k] + M3[k][j])

    f = open('m3.txt', 'w')

    # From matrix to .txt-file
    for row in M3:
        for cell in row:
            f.write("{0:2d}".format(cell))
        f.write("\n")

    f.close()
    return M3
    

G, M1 = readFromAdjacencyMatrix()
M2 = writeToIncidenceMatrix(G, M1)
M3 = writeToDistanceMatrix(G, M1)
##prettyPrint(M1)
##prettyPrint(M2)
##prettyPrint(M3)

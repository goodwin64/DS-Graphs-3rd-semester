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

def readFromAdjacencyMatrix(G=Graph()):
    Matrix = []
    f = open('m1.txt', 'r')
    for line in f:
        Matrix.append( list( map( int, line.split())) )

    for row in range(1, len(Matrix)+1):
        for cell in range(1, len(Matrix)+1):
            if Matrix[row-1][cell-1] != 0:
                G.addEdge(row, cell)

    f.close()
    return G, Matrix

def writeToIncidenceMatrix(G, M1):
    '''M1 - матрица смежности, которую мы читаем с файла
       M2 - матрица инцидентности, которую мы создаем и записываем в новый файл
    '''
    edges = countEdges(M1)

    M2 = [[0 for i in range(edges)] for j in range(len(G.vertList))]
                
    f = open('m2.txt', 'w')
    c = 0
    for i in range(0, len(M1)):
        for j in range(0, i+1):
            if M1[i][j] == 1:
                M2[i][c] = 1
                M2[j][c] = 1
                c += 1

    for row in M2:
        for cell in row:
            f.write("%d " % cell)
        f.write("\n")

    f.close()
    return M2

G, M1 = readFromAdjacencyMatrix()
M2 = writeToIncidenceMatrix(G, M1)

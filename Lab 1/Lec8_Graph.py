from random import randint

class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
        self.distance = 0
        self.color = "white"
        self.pred = None

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return "Vertex: id=%d" % self.id

    def printConnections(self):
        return str(self.id) + ' соединен с: \n' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

    def setDistance(self, dist):
        self.distance = dist

    def getDistance(self):
        return self.distance

    def setPred(self, pred):
        self.pred = pred

    def getPred(self):
        return self.pred

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

class Graph:
    def __init__(self, oriented=False):
        self.vertList = {}
        self.edgeList = []
        self.numVertices = 0
        self.orient = oriented

    def __iter__(self):
        return iter(self.vertList.values())

    def __str__(self):
        return "Graph: size=%d" % (self.numVertices)

    def __contains__(self,key):
        return key in self.vertList

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        #return newVertex

    def deleteVertex(self, key):
        del self.vertList[key]
        self.numVertices -= 1

    def getVertex(self, key):
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None

    def addVertices(self, minID=1, maxID=10):
        for i in range(minID, maxID+1):
            G.addVertex(i)

    def deleteVertices(self, minID=5, maxID=7):
        for i in range(minID, maxID+1):
            G.deleteVertex(i)
    
    def addEdge(self,from_key,to_key,edgeKey=1,cost=1):
        if from_key not in self.vertList:
            nv = self.addVertex(from_key)
        if to_key not in self.vertList:
            nv = self.addVertex(to_key)
        fr = self.vertList[from_key]
        to = self.vertList[to_key]
        fr.addNeighbor(to, cost)
        self.edgeList.append([edgeKey, from_key])
        self.edgeList.append([edgeKey, to_key])
        if not self.orient:
            to.addNeighbor(fr, cost)
        #self.vertList[from_key].addNeighbor(self.vertList[to_key], cost) # - It's the same action, but written in one row

    def addRandEdge(self, maxCost=10):
        minID = min(self.vertList.keys())
        maxID = max(self.vertList.keys())
        self.addEdge(randint(minID, maxID), randint(minID, maxID), randint(1, maxCost))
    
    def getVertices(self):
        return self.vertList.keys()

    def addSomeEdges(self):
        keys = self.vertList.keys()
        for even in keys:
            for odd in keys:
                if even % 2 == 0\
                   and odd % 2 == 1\
                   and even in G.vertList\
                   and odd in G.vertList\
                   and abs( odd - even ) <= 2:
                    self.addEdge(odd, even)

    def printAllConnections(self):
        for key in self.vertList.keys():
            print(self.vertList[key].printConnections())

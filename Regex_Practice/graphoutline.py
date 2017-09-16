class Vertex:
    def __init__(self, key):
        self.id = key
        #vertex ID
        self.edgeWith = {}
        #edge this vertex has with other vertices
        #stored in dict
    
    def addNeighborVertex(self, neighbor, weight):
        self.edgeWith[neighbor] = weight
        #in my notes weight = 0 was the last argument, but I don't think this needs to be a weighted graph
        #but this will need a rewrite
        
    def getNeighbors(self):
        for key, value in self.edgeWith.items():
            print(self)
        #python 3 weirdness, reworking
        
    def getID(self):
        return self.id
        
    def __str__(self):
        return str(self.id) + ' has an edge with ' + str([x.id for x in self.edgeWith])
        #ex: VertexB has an edge with VertexC
        #go through list of keys in self.edgeWith

class Graph:
    def __init__(self):
        self.verticeDict = {}
        #dictionary of vertices in graph
        self.numVertices = 0
        #initialize to zero
        
    def addVertex(self, key):
        self.numVertices += 1 
        #increment count of vertices when adding a vertex
        newVertex = Vertex(key)
        #create a new Vertex object
        self.verticeDict[key] = newVertex
        #put vertex obj into dictionary
        return newVertex
        
    def getVertex(self, n):
        if n in self.verticeDict:
            #search keys
            return self.verticeDict[n]
        else:
            return None
            
    def addEdge(self, fromVert, toVert, weight):
        if fromVert not in self.verticeDict:
            nv = self.addVertex(fromVert)
        if toVert not in self.verticeDict:
            self.addVertex(toVert)
        
        self.verticeDict[fromVert].addNeighborVertex(self.verticeDict[toVert], weight)
        #add the 'to vertex' as a neighbor of 'from vertex' by accessing it in the dictionary via
        #its key
        
    def getVertices(self):
        return self.verticeDict.keys()
        #return keys of all vertices in graph
    
    def __iter__(self):
        return iter(self.verticeDict.values())
        #iterate through values
        
    def __contains__(self, n):
        return n in self.verticeDict
        #bool
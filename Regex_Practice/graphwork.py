from graphoutline import *

g = Graph()

for i in range(6):
    g.addVertex(i)
    #add 6 vertices
    
g.addEdge(0,1,0)
#from vertex 0, to vertex 

for vertex in g:
    print(vertex.getNeighbors())
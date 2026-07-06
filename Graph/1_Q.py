#Route Between Nodes:
#-Problem statement:
 #  -Given a directed graph and two nodes (S and E) design an algorithm to find out whther there is a route from S to E

#**PsuedoCode
#   -Create function with two parameters start and end nodes.
#   -Create queue and enqueue start node to it.
#   -Find all the neighbourse of the just enqueued node and enqueue them into the quueue.
#   -Repeat this process until the end of elements in graph.
#   -If during the above process at some point in time we encounter the destination node, we return True.
#   -Mark visisted nodes as visited.

class Graph :
    def __init__(self, gdict=None):
        if gdict is None:
            gdict={}
        self.gdict=gdict

    def addEdges(self, vertex, edges):
        self.gdict[vertex].append[edges]

    def checkRoute(self, startNode, endNode):
        visited=[startNode]
        queue = [startNode]
        path = False
        while queue:
            deVertex=queue.pop(0)
            for adjacentVertex in self.gdict[deVertex]:
                if adjacentVertex not in visited:
                    if adjacentVertex == endNode:
                        path=True
                        break
                    else:
                        visited.append(adjacentVertex)
                        queue.append(adjacentVertex)
        return path
    

customDict = { "a" : ["c","d", "b"],
               "b" : ["j"],
               "c" : ["g"],
               "d" : [],
               "e" : ["f", "a"],
               "f" : ["i"],
               "g" : ["d", "h"],
               "h" : [],
               "i" : [],
               "j" : []
             }

g = Graph(customDict)
print(g.checkRoute("a", "e"))
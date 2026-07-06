from collections import defauldict   

class Graph:
    def __init__(self, numberofVertices):
        self.graph=defauldict(list)
        self.numberofVertices=numberofVertices


    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)    

    def topologicalSort(self, v, visited, stack):
        visited.append(v)           

        for i in self.graph[v]:
            if i not in visited:
                self.topologicalSort(i, visited, stack)

        stack.insert(0,v)

    def topologicalSort(self):

        visited=[]
        stack=[]

        for k in list(self.graph):
            if k not in visited:
                self.topologicalSort(k, visited, stack)

        print(stack)

customGraph = Graph(8)

customGraph.addEdge("A", "C")
customGraph.addEdge("C", "E")
customGraph.addEdge("E", "H")
customGraph.addEdge("E", "F")
customGraph.addEdge("F", "G")
customGraph.addEdge("B", "D")
customGraph.addEdge("B", "C")
customGraph.addEdge("D", "F")                                                                                                                                                                                                                                                                                                                                                                                                                                                            
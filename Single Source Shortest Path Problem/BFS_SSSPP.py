 
class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict={}
        self.gdict=gdict


    def bfs(self, start, end):
        queue=[]
        queue.append([start])
        while queue:
            path = queue.pop(0)
            node=path[-1]
            if node == end:
                return path
            for adjacent in self.gdict.get(node, []):
                new_Path=list(path)
                new_Path.append(adjacent)
                queue.append(new_Path)


Custimdict={"A": ["B", "C"],
          "B":["D", "G"],
          "C":["D", "E"],
          "D":["F"],
          "E":[ "F"],
          "G":["F"]
          }

g = Graph(Custimdict)
print(g.bfs("A", "F"))
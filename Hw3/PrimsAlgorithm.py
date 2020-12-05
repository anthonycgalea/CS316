import sys

class Node:
    def __init__(self, adjMat, key, graph):
        self.adjMat = adjMat.split()
        self.included = False
        self.key = key
        self.vertices = []
        self.graph = graph
        for k in range(len(self.adjMat)):
            #print(self.adjMat)
            if (not int(self.adjMat[k]) == 0):
                self.vertices.append(k)
    def findMin(self, currVert, currMin, currKeyNode):
        if (not self.included):
            return [currVert, currMin, currKeyNode]
        min = currMin
        minVert = currVert
        for k in range(len(self.vertices)):
            if (int(self.adjMat[self.vertices[k]]) < min and int(self.adjMat[self.vertices[k]]) > 0 and not self.graph.nodes[self.vertices[k]].included):
                min = int(self.adjMat[self.vertices[k]])
                minVert = self.vertices[k]
                currKeyNode = self.key
        return [minVert, min, currKeyNode]



class Graph:
    def __init__(self, lines):
        self.nodes = []
        for k in range(len(lines)):
            self.nodes.append(Node(lines[k], k, self))
            self.root = self.nodes[0]
            self.nodes[0].included = True
    def genPrims(self):
        self.newAdjMat = []
        for a in range(len(self.nodes)):
            addMat = []
            for b in range(len(self.nodes)):
                addMat.append(0)
            self.newAdjMat.append(addMat)
        for k in range(len(self.nodes)-1):
            min = sys.maxsize
            currKeyNode = -1
            currVert = -1
            info = [currVert, min, currKeyNode]
            for l in range(len(self.nodes)):
                info = self.nodes[l].findMin(info[0], info[1], info[2])
            currVert = info[0]
            min = info[1]
            currKeyNode = info[2]
            self.nodes[currVert].included = True
            self.newAdjMat[currVert][currKeyNode] = min
            self.newAdjMat[currKeyNode][currVert] = min
    def printMat(self):
        for k in range(len(self.newAdjMat)):
            s = ""
            for l in range(len(self.newAdjMat[k])):
                s= s + str(self.newAdjMat[k][l]) + " "
            print(s)
fileName = input("Enter graph file:\t")

f = open(str(fileName), 'r')
lines = f.read().split('\n')
print(lines)
            
g = Graph(lines)
g.genPrims()
g.printMat()
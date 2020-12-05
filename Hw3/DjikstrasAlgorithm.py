import sys

class Node:
    def __init__(self, adjMat, key, graph):
        self.adjMat = adjMat.split()
        self.included = False
        self.key = key
        self.children = []
        self.childWeights = []
        self.graph = graph
        for k in range(len(self.adjMat)):
            #print(self.adjMat)
            if (not int(self.adjMat[k]) == 0):
                self.children.append(k)
                self.childWeights.append(int(self.adjMat[k]))
    def findMin(self, destination, visited, count=-5):
        nVisited = [] #making a copy of visited
        if (count==-5):
            count = len(self.graph.nodes)
        for k in range(len(visited)):
            nVisited.append(visited[k])
        nVisited[self.key] = 1
        addWeight = sys.maxsize
        for k in range(len(self.children)):
            if (int(self.children[k]) == destination):
                addWeight = self.childWeights[k]
        for k in range(len(self.children)):
            checkAdd = 0
            if (nVisited[self.children[k]] == 0 or count >=0):
                checkAdd = self.childWeights[k] + self.graph.nodes[self.children[k]].findMin(destination, nVisited, count-1)
            if addWeight > checkAdd:
                addWeight = checkAdd
        return addWeight



class Graph:
    def __init__(self, lines):
        self.nodes = []
        self.nodeNames = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for k in range(len(lines)):
            self.nodes.append(Node(lines[k], k, self))
            self.root = self.nodes[0]
            self.nodes[0].included = True
    def genFreshVisited(self):
        visited = []
        for k in range(len(self.nodes)):
            visited.append(0)
        return visited
    def genDjik(self):
        self.dists = []
        for k in range(len(self.nodes)-1):
            self.dists.append(self.root.findMin(k+1, self.genFreshVisited()))
    def printInfo(self):
        for k in range(len(self.dists)):
            print("Source -> Node " + self.nodeNames[k] + ":\t" + str(self.dists[k]))
fileName = input("Enter graph file:\t")

f = open(str(fileName), 'r')
lines = f.read().split('\n')
print(lines)
            
g = Graph(lines)
g.genDjik()
g.printInfo()
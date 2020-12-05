class Node():
    def __init__(self, char, num):
        self.num = num
        self.left = None
        self.right = None
        self.char = char
        self.huffCode = None

    def generateHuff(self, currValue):
        if (not self.left == None):
            self.left.generateHuff(currValue+"0")
        if (not self.right == None):
            self.right.generateHuff(currValue+"1")
        self.huffCode = currValue
    
    def addLeft(self, node):
        self.left = node

    def addRight(self, node):
        self.right = node
    
    def addOne(self):
        self.num = self.num+1
    
    def printHuff(self):
        if (not self.char == None):
            if (self.char == " "):
                print("<sp>:\t" + self.huffCode)
            else:
                print(self.char + ":\t" + self.huffCode)
        if (not self.left == None):
            self.left.printHuff()
        if (not self.right == None):
            self.right.printHuff()
    
    def huffLength(self):
        length = len(self.huffCode)
        return length

word = input("Please give an input word:\t")
nodes = []
charNodes = []
word = word.lower()
for k in range(len(word)):
    newNode = True
    for l in range(len(nodes)):
        if nodes[l].char == word[k]:
            newNode = False
            nodes[l].addOne()
    if (newNode):
        nodes.append(Node(word[k], 1))
        charNodes.append(nodes[-1])

while(len(nodes) > 1):
    min1 = nodes[0]
    min2 = nodes[1]
    for k in range(len(nodes)-2):
        k = k+2
        if (nodes[k].num < min1.num):
            if (min1.num > min2.num):
                min2 = nodes[k]
            else:
                min1 = nodes[k]
        elif(nodes[k].num < min2.num):
            min2 = nodes[k]
    nodes.append(Node(None, min1.num + min2.num))
    nodes[-1].addLeft(min1)
    nodes[-1].addRight(min2)
    nodes.remove(min1)
    nodes.remove(min2)

nodes[0].generateHuff("")
nodes[0].printHuff()

totLength = len(word)*8
compLength = 0
for k in range(len(word)):
    char = word[k]
    for l in range(len(charNodes)):
        if (charNodes[l].char == char):
            add = charNodes[l].huffLength()
            compLength=compLength+add

print("Compression ratio:\t("+str(compLength)+"/"+str(totLength)+")")

    
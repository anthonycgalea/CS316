class Node():
    value = 0
    def __init__(self, value): 
        self.right = None
        self.left = None
        self.value = value
    def LVR(self):
        if (self.left != None):
            self.left.LVR()
        print(str(self.value))
        if (self.right != None):
            self.right.LVR()
    def RVL(self):
        if (self.right != None):
            self.right.RVL()
        print(str(self.value))
        if (self.left != None):
            self.left.RVL()
    def VLR(self):
        print(str(self.value))
        if (self.left != None):
            self.left.VLR()
        if (self.right != None):
            self.right.VLR()
    def VRL(self):
        print(str(self.value))
        if (self.right != None):
            self.right.VRL()
        if (self.left != None):
            self.left.VRL()
    def LRV(self):
        if (self.left != None):
            self.left.LRV()
        if (self.right != None):
            self.right.LRV()
        print(str(self.value))
    def RLV(self):
        if (self.right != None):
            self.right.RLV()
        if (self.left != None):
            self.left.RLV()
        print(str(self.value))
    def addLeft(self, node):
        if (self.left == None):
            self.left = node
        else:
            self.left.add(node)
    def addRight(self, node):
        if (self.right == None):
            self.right = node
        else:
            self.right.add(node)
    def add(self, node):
        if (node.value < self.value):
            self.addLeft(node)
        else:
            self.addRight(node)

class BST():
    def __init__(self):
        self.root = None
    def addNode(self, node):
        if (self.root == None):
            self.root = node
        else:
            self.root.add(node)
    def LVR(self):
        if (self.root != None):
            self.root.LVR()
        else:
            print("No nodes found.")
    def RVL(self):
        if (self.root != None):
            self.root.RVL()
        else:
            print("No nodes found.")
    def VLR(self):
        if (self.root != None):
            self.root.VLR()
        else:
            print("No nodes found.")
    def VRL(self):
        if (self.root != None):
            self.root.VRL()
        else:
            print("No nodes found.")
    def LRV(self):
        if (self.root != None):
            self.root.LRV()
        else:
            print("No nodes found.")
    def RLV(self):
        if (self.root != None):
            self.root.RLV()
        else:
            print("No nodes found.")


bst = BST()
while(True):
    print("Welcome to the BST traversal tool! Add nodes by entering a number, check traversals by entering the following codes:")
    print("LVR: i")
    print("RVL: ii")
    print("VLR: iii")
    print("VRL: iv")
    print("LRV: v")
    print("RLV: vi")
    print("Quit: x")
    user = input("Please make a selection:\t")
    user = user.lower()
    if (user.isnumeric()):
        n = Node(int(user))
        bst.addNode(n)
    else:
        if (user == "i"):
            bst.LVR()
        elif(user == "ii"):
            bst.RVL()
        elif(user == "iii"):
            bst.VLR()
        elif(user == "iv"):
            bst.VRL()
        elif(user == "v"):
            bst.LRV()
        elif(user == "vi"):
            bst.RLV()
        elif(user == "x"):
            break
        else:
            print("Invalid entry. Please try again.")
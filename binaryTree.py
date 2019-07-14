class Node():
    def __init__(self, data=None, leftChild=None, rightChild=None):
        self.data = data 
        self.leftChild = leftChild
        self.rightChild = rightChild

class BinarySearchTree():
    def __init__(self): 
        self.rootNode = Node()
    def insertChildNode(self, nodeBeingInserted, currentNode, previousNode=None):
        if currentNode == None: 
            if nodeBeingInserted.data <= previousNode.data:
                previousNode.leftChild = nodeBeingInserted
            else:
                previousNode.rightChild = nodeBeingInserted
            return previousNode
        if nodeBeingInserted.data <= currentNode.data:
            self.insertChildNode(nodeBeingInserted, currentNode.leftChild, currentNode)
        else:
            self.insertChildNode(nodeBeingInserted, currentNode.rightChild, currentNode)

    def create(self):
        while True:
            if self.rootNode.data==None:
                print("Enter the data for the head/root node of the tree")
                data = float(input())
                self.rootNode.data = data
            else:
                print("Enter the data for the child node of the tree")
                data=float(input())
                childNode = Node(data)
                self.insertChildNode(childNode, self.rootNode)

            print('Do you want to enter more children nodes ?')
            ch=input()
            if ch not in ['y', 'Y', 'yes', 'YES', 'Yes', 'yea', 'YEA', 'Yea']:
                break
            else:
                continue

    def display(self, currentNode):
    #Depth First Search Display
        if currentNode == None:
            print("None")
            return
        print(currentNode.data)
        self.display(currentNode.leftChild)
        self.display(currentNode.rightChild)

    def depth(self, node, currentNode, depth=0):
        if currentNode == None:
            return False
        elif currentNode == node:
            return depth
        else:
            return self.depth(node, currentNode.leftChild, depth+1) or self.depth(node, currentNode.rightChild, depth+1)

bst1 = BinarySearchTree()
bst1.create()
# bst1.display(bst1.rootNode)
print(bst1.depth(bst1.rootNode.rightChild, bst1.rootNode))
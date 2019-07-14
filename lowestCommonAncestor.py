class Node():
    def __init__(self, data=None):
        self.data = data
        self.children = []
        self.noOfChildren = 0

class Tree: 

    def __init__(self):
        self.rootNode = None

    def create(self):
        if self.rootNode == None:
            print('Enter the data for the root node')
            data = input()
            self.rootNode = Node(data)
            self.insertChildrenRecusively(self.rootNode)

    def insertChildrenRecusively(self, node):
        print('Do you want to enter children for "{parentNodeName}" '.format(parentNodeName=node.data))
        choice = input()
        if(choice in ['y', 'yes', 'Y', 'Yes', 'YES']):
            self.insertChildren(node)
            for child in node.children:
                self.insertChildrenRecusively(child)
        else:
            return 

    def insertChildren(self, node):
        choice = ''
        while choice not in ['no', 'n', 'No', 'nO', 'N', 'NO']:
            print('Enter the data for the child of "{parentNodeName}" '.format(parentNodeName=node.data))
            data = input()
            childNode = Node(data)
            node.children.append(childNode)
            node.noOfChildren+=1
            print('Do you want to enter more children for "{parentNodeName}"?'.format(parentNodeName=node.data))
            choice = input()

    def display(self, node):
        if(node.children == []):
            print("----------"*2)
            print('Parent Node: {parentNode}'.format(parentNode=node.data))
            print("It's children: ", node.children)
            print("----------"*2)
            return 
        else:
            print("----------"*2)
            print('Parent Node: {parentNode}'.format(parentNode=node.data))
            print("It's children:")
            childrenDataArray = []
            for child in node.children:
                childrenDataArray.append(child.data)
            print(childrenDataArray)
            print("----------"*2)
            
            for child in node.children:
                self.display(child)

    def pathToNode(self, root, node, path=None):
        if path==None:
            path=[]
        if root.children==[]:
            return 
        if node in root.children:
            path.append(root.data)
            return path
        else:
            for iter_node in root.children:
                iter_path = iter_node.data
                self.pathToNode(iter_node, node, iter_path)
        


uber = Tree()
uber.create()
uber.display(uber.rootNode)

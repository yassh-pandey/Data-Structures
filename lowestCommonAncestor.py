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

    def pathToNode(self, root, node, pathDict=None):
        if pathDict==None:
            pathDict={
                "path": [],
                "found": False
            }
        pathDict["path"].append(root.data)
        if root == node:
            pathDict["found"] = True
            return pathDict["path"]
        if pathDict["found"]:
            return pathDict["path"]
        elif root.children==[]:
            pathDict["path"].pop()
            return pathDict["path"]
        elif node in root.children:
            pathDict["found"] = True
            return pathDict["path"]
        else:
            for iter_node in root.children:
                if not pathDict["found"]:
                    finalPath = self.pathToNode(iter_node, node, pathDict)
            return finalPath
        
    def lca(self, node1, node2):
        path1 = self.pathToNode(self.rootNode, node1)
        path2 = self.pathToNode(self.rootNode, node2)
        for nodeElement1 in path1[::-1]:
            for nodeElement2 in path2[::-1]:
                if(nodeElement2 == nodeElement1):
                    return nodeElement1


uber = Tree()
uber.create()
uber.display(uber.rootNode)
print(uber.pathToNode(uber.rootNode, uber.rootNode.children[0].children[1].children[0]))
print(uber.pathToNode(uber.rootNode, uber.rootNode.children[0].children[2]))
print(uber.lca(uber.rootNode.children[0].children[1].children[0], uber.rootNode.children[0].children[2]))
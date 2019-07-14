class Node():
    def __init__(self, data=0, left=None, right=None, up=None, down=None):
        self.data = data
        self.left = left
        self.right = right
        self.up = up
        self.down = down
    def isHeadNode(self):
        return self.left == None and self.right != None


class LinkedList():
    def __init__(self):
        self.headNode = None
        self.length = 0
        self.end = None

    def create(self):
        while True:
            print("Enter the Node data")
            data = float(input())
            if self.headNode == None:
                pnode = Node(data)
                self.headNode = pnode
                self.end = self.headNode
                self.length += 1
            else:
                newNode = Node(data)
                self.end.right = newNode
                newNode.left = self.end
                self.end = newNode
                self.length += 1
            print("Do you wish to continue (Y or N)")
            ch = input()
            if ch == 'N' or ch == 'n':
                break
    def display(self):
        cnode = self.headNode
        while cnode.right != None:
            print(cnode.data, end=' -> ')
            cnode = cnode.right
        print(cnode.data)


# x = LinkedList()
# x.create()
# x.display()
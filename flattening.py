from linkedList1 import Node, LinkedList
class ThickLinkedList(LinkedList):
    def __init__(self):
        self.headNode=None
        self.end = None
    def createThickLinkedList(self):
        while True:
            print("Enter the data for the Thick Linked List element")
            data = float(input())
            if(self.headNode==None):
                parentNode = Node(data)
                self.headNode = parentNode
                self.end = self.headNode
            else:
                newNode = Node(data)
                self.end.right = newNode
                self.end = newNode
            print("Enter the down linked list (leg) for this backbone node")
            downLL = LinkedList()
            downLL.create()
            currentNode = self.end
            currentNode.down = downLL
            print('Do you want to enter a new node to the thick linked list\'s backbone (Y or N)')
            ch = input()
            if ch=='n' or ch=='N':
                break

    def displayThickLinkedList(self):
        print("The backbone of the Thick Linked List is")
        self.display()
        print('The respective legs of the Thick Linked List are')
        currentNode = self.headNode
        while currentNode.right != None:
            currentNode.down.display()
            currentNode = currentNode.right
        currentNode.down.display()
    
    def flatten(self):
        returnedLinkedList = LinkedList()
        currentNode = self.headNode
        while True:
            if currentNode == None:
                return returnedLinkedList
            else:
                if returnedLinkedList.headNode == None:
                    flatNode = Node(currentNode.data)
                    returnedLinkedList.headNode = flatNode
                    returnedLinkedList.end = returnedLinkedList.headNode
                    returnedLinkedList.length += 1
                else:
                    flatNode = Node(currentNode.data)
                    returnedLinkedList.end.right = flatNode
                    returnedLinkedList.end = flatNode
                    returnedLinkedList.length += 1
                
                down = currentNode.down.headNode
                while True:
                    if down == None:
                        break
                    else:
                        downNode = Node(down.data)
                        returnedLinkedList.end.right = downNode
                        returnedLinkedList.end = downNode
                        returnedLinkedList.length += 1
                        down = down.right

                currentNode = currentNode.right
                   

            

tll = ThickLinkedList()
tll.createThickLinkedList()
tll.displayThickLinkedList()
flatLinkedList = tll.flatten()
print("Thick Linked List after flattening looks like this:")
flatLinkedList.display()

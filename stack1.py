class Stack():

    def __init__(self, *args):
        self.list = list(args)

    def push(self, item):
        self.list.append(item)

    def display(self):
        for index, item in enumerate(self.list):
            if index == ( len(self.list) - 1 ):
                print("{}".format(item))
            else:
                print("{} ->".format(item), end=" ")

    def pop(self):
        if self.isEmpty():
            print("Stack is empty so can't perform pop operation !")
        else:
            return self.list.pop()

    def top(self):
        if self.isEmpty():
            print("Stack is empty so top operation will return null !")
        else:
            return self.list[-1]
    
    def isEmpty(self):
        return len(self.list) == 0


# l = Stack()
# l.push(1)
# l.push(2)
# l.push(3)
# l.pop()
# l.pop()
# l.pop()
# print(l.isEmpty())
# l.pop()






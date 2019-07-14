from stack1 import Stack
print('Enter the string')
string = input()
s = Stack()

for char in string:
    s.push(char)

print("Reversing string")
while not s.isEmpty():
    print(s.pop(), end="")
class Stack:
    def __init__(self,size):
        self.__top = -1
        self.__size = size
        self.__elements = [None] * size

    def size(self):
        return self.__top + 1

    def isFull(self):
        return self.size() == self.__elements
    def isEmpty(self):
        return self.size() == 0

    def peek(self):
        if self.isEmpty():
            print("Stack has no element")
            exit(1)
        return self.__elements[self.__top]

    def push(self,value):
        if self.isFull():
            print("Stack is full")
            exit(1)
        print("Inserting",value,"in stack")
        self.__top = self.__top + 1
        self.__elements[self.__top] = value

    def pop(self):
        if self.isEmpty():
            print("Stack has no value")
            exit(1)
        print("Removing",self.peek(),"from stack")
        top = self.__elements[self.__top]
        self.__top = self.__top - 1
        return top

stack = Stack(5)
stack.push("ravi")
stack.push("varma")
stack.push("gokull")
stack.push("ganesh")
stack.push("nandha")


stack.pop()
stack.pop()
stack.pop()
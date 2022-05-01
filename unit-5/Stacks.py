class Stack:
    # defining the initializer
    def __init__(self):
        # elements is an empty list at first to store the elements to be added to the stack
        # elements is a property of the stack
        self.elements = [] # it is a traditional list (array)

    # isEmpty() definition
    # Returns True if the stack is empty
    def isEmpty(self):
        # determine the number of elements saved in the list
        numberofElements = len(self.elements)
        # Check whether numberofElements = 0
        if numberofElements == 0:
            return True
        else:
            return False

    # peek() definition
    # Returns the element on the top of the stack without removing it from the stack
    def peek(self):
        if self.isEmpty():
            return None
        else:
            # Returning the last element added to the list
            # for a list of three elements they are indexed as: 0, 1, 2
            # This means the index of the last element is 2 = (size of list (3) - 1)
            return self.elements[len(self.elements) - 1]
            # indextoReturn = len(self.elements) - 1
            # return self.elements[indextoReturn]


    # push(value) definition
    # Adds value to the top of the stack (adds value to the elements list)
    def push(self, value):
        self.elements.append(value)

    # pop() definition
    # Returns the element from the top of the stack
    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.elements.pop()

    # getSize() definition
    # Returns the size of the stack
    def getSize(self):
        return len(self.elements)

    def decToBinary(self, number):
        st = Stack()
        x = int(number)
        while(x!=0):
            st.push(int(x%2))
            x = int(x/2)
        binary = ""
        while(not st.isEmpty()):
            binary+=str(st.pop())
        return binary

    def reverseString(self, myString):
        reverse = []
        res = myString.split()
        i = len(res) - 1
        for a in range(i, -1, -1):
            reverse.append(res[a])
        return " ".join(reverse)

def main():

    # create a stack
    mystack = Stack()
    number = int(input("Enter the number you want to convert: "))
    my_result = mystack.decToBinary(number)
    print(my_result, " is the binary representation of ", number)

    myStringStack = Stack()
    myString = input("Enter the String You Want to Reverse: ")
    print("Reversed: ", myStringStack.reverseString(myString))

main()

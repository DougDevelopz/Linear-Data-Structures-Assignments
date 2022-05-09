class Stack:
    # defining the initializer
    def __init__(self):
        # elements is an empty list at first to store the elements to be added to the stack
        # elements is a property of the stack
        self.elements = []  # it is a traditional list (array)

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


def CheckAnswers(stack1, stack2):
    if stack1.getSize() is not stack2.getSize():
        return "Error"
    n = 0
    while not stack1.isEmpty():
        if stack1.pop() == stack2.pop():
            n = n + 1
    return n

'''
1 - Initialize a counter
2 - Use pop() to compare elements from both stacks
3 - If the elements popped are the same, then increment the counter
4 - return the counter at the end
'''


##########################
### Write your code here
##########################


def main():
    '''
    1 - Create stack1 to hold the answer key - DONE FOR YOU
    2 - Ask the user to enter the answer key
    3 - Create stack2 to hold the solution to be checked - DONE FOR YOU
    4 - Ask the user to enter the solution to be checked
    5 - Use push() to fill the stacks
    6 - Call the function - DONE FOR YOU
    '''

    stack1 = Stack()  # stack1 will hold the answer key
    s1 = input("Please answer the key separated by space: ")
    whitespaceS1 = s1.split()
    for e in whitespaceS1:
        stack1.push(e)
    stack2 = Stack()  # stack2 will hold the solution to be checked
    s2 = input("Please enter the answers to be checked separated by space: ")
    whitespaceS2 = s2.split()
    for e in whitespaceS2:
        stack2.push(e)


    ##############################################
    ### Write your code here for steps: 2,4,5 ####
    ##############################################

    result = CheckAnswers(stack1, stack2)
    print("The total score is: ", result)


main()

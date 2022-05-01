# Defining the Node Class
# Defines how the node will look like

class Node:
    def __init__(self, e): # "e" represents the element in the node
        self.element = e
        self.next = None


# Class definition of LinkedList
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # addFirst Implementation
    # Adds an element to the beginning of the linked list
    def addFirst(self, e):
        newNode = Node(e) # Creating a new Node
        newNode.next = self.head # link the new Node to the head list
        self.head = newNode # head now points to the new node
        self.size = self.size + 1 # update the size of the list

    # addLast Implementation
    # Adds an element to the end of the list
    def addLast(self, e):
        newNode = Node(e) # Creating a new Node
        if self.tail == None:
            self.head = self.tail = newNode # The list was empty and now it will have the only node
        else:
            self.tail.next = newNode # Linked the new Node with the last node of the list (the tail)
            self.tail = self.tail.next # Tail now points to the last node
        self.size += 1 #update the size


    # add Implementation
    # Adds new nodes to the linked list
    def add(self, e):
        self.addLast(e)

    # insert Implementation
    # Inserts a new element at a specified index in the list
    def insert(self, index, e):
        newNode = Node(e)
        if index == 0:
            self.addFirst(e)
        elif index >= self.size:
            self.addLast(e)
        else:
            current = self.head
            for i in range (1, index):
                current = current.next
            temp = current.next
            current.next = newNode
            (current.next).next = temp
            self.size += 1


    # removeFirst Implementation
    # Removes the first node in the linked list (the head)
    # returns the object that is contained in the removed node
    def removeFirst(self):
        if self.size == 0:
            return None # nothing is there to remove
        else:
            temp = self.head # keep the first node temporarily
            self.head = self.head.next # Move the head of the list to the next node in the list
            self.size -= 1 # Reduce the size by 1
            if self.head == None: # if thhe list gets empty after removing the node
                self.tail = None
            return temp.element

    # removeLast Implementation
    # Removing the last node from the list
    # return the object that is saved in the node before removing it
    def removeLast(self):
        if self.size == 0: # if the list is empty
            return None # nothing to return
        elif self.size == 1: # In the case of one element in the list
            temp = self.head
            self.head = self.tail = None # List becomes empty
            self.size = 0 # updating the size to 0
            return temp.element # returning the element from the deleted node
        else: # the list has more than 1 node
            current = self.head

            for i in range(self.size - 2): # navigating to the 2nd to last node in the list
                current = current.next

            temp = self.tail # Saving the tail
            self.tail = current # Update the current tail
            self.tail.next = None
            self.size -= 1
            return temp.element

    # removeAt Implementation
    # Removes the element at a particular index in the list
    # returns the removed element
    def removeAt(self, index):
        if index < 0 or index >= self.size:
            return None # Index is out of range
        elif index == 0:
            return self.removeFirst() # remove the first node in the list
        elif index == self.size - 1:
            return self.removeLast() # remove the last node in the list
        else:
            previous = self.head

            for i in range(1, index):
                previous = previous.next

            current = previous.next
            previous.next = current.next
            self.size -= 1
            return current.element

    # getFirst Implementation
    # Returns the first element of the first node in the list
    def getFirst(self):
        if self.size == 0: #list is empty
            return None
        else:
            return self.head.element

    # getLast Implementation
    # Returns the last element of the last node in the list
    def getLast(self):
        if self.size == 0: # List is empty
            return None
        else:
            return self.tail.element

    # indexOf Implementation
    # Returns the index of the matching element in the list
    # Returns -1 if there is no match
    def indexOf(self, e):
        current = self.head
        i = 0 # variable that will keep track of the index you are looking for

        while current != None:
            if current.element == e:
                return i
            i += 1
            current = current.next

        return -1

    # clear Implementation
    # Clears the linked list
    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    # contain Implementation
    # returns true if the linked list has the element "e"
    def contains(self, e):
        if self.indexOf(e) >= 0:
            return True
        else:
            return False


    # Remove Implementation
    # Remove the element from the list
    def remove(self,e):
        index = self.indexOf(e) # finding the index of the element to be deleted
        if index == -1:
            return False
        else:
            self.removeAt(index)
        return True

    # toString Implementation
    # returns the linked list a string of elements denoted by list notation [e1,e2,e3]
    def toString(self):
        result = "[" # Beginning of the list notation

        current = self.head
        for i in range(self.size):
            result += str(current.element)
            current = current.next
            if current != None:
                result += ", " # separate between the elements
            else:
                result += "]" # Insert the closing ] of the string

        return result

    # set Implementation
    # Replaces the element at the specified index with your own element
    def set(self, index, e):
        if index < 0 or index >= self.size:
            print("Index is out of range")
            return None

        # You are iterating to arrive at the node you are looking for at the index
        current = self.head
        for i in range(index):
            current = current.next

        # current represents the node you are looking for
        current.element = e

    # isEmpty Implementation
    # Checks whether the list is empty
    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False
    # getSize Implementation
    # Returns the size of the list
    def getSize(self):
        return self.size
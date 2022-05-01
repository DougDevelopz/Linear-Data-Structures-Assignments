from LinkedList import LinkedList

class Queue:
    # Define the initializer
    # Use Linked list as main structure to form the queue
    def __init__(self):
        self.elements = LinkedList()

    # enqueue(e) definition
    # Adds an element to the queue
    def enqueue(self,e):
        self.elements.add(e)

    # dequeue() implementation
    # Removes an element from the queue
    def dequeue(self):
        if self.elements.getSize() == 0:
            return None
        else:
            # remove from the head of the linked list forming the queue
            return self.elements.removeAt(0)

    # getSize() implementation
    # Returns the size of the queue
    def getSize(self):
        return self.elements.getSize()

    # isEmpty() implementation
    # Returns True if the queue is empty
    def isEmpty(self):
        if self.elements.getSize() == 0:
            return True
        else:
            return False

    # toString() implementation
    # Return the queue in a string format
    def toString(self):
        return self.elements.toString()


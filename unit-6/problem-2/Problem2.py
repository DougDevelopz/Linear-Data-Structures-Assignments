from LinkedList import LinkedList
from Queues import Queue
from Stacks import Stack


# Function definition to reverse the queue
def reversequeue(myqueue):
    mystack = Stack()

    while not myqueue.isEmpty():
        mystack.push(myqueue.dequeue())
    while not mystack.isEmpty():
        myqueue.enqueue(mystack.pop())
    ''' WRITE FUNCTION IMPLEMENTATION HERE'''
    ''' DONT'T FORGET TO USE STACK AND QUEUES'''

    return myqueue


## DO NOT CHANGE THE MAIN ##
def main():
    myqueue = Queue()
    myqueue.enqueue("A")
    myqueue.enqueue("B")
    myqueue.enqueue("C")
    myqueue.enqueue("D")
    myqueue.enqueue("E")
    print("Before Reversing: ", myqueue.toString())
    print("After Reversing: ", reversequeue(myqueue).toString())


main()

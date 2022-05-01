from Queues import Queue


# Assignment Problem #1
# Generate Binary numbers from 1 to n


def main():
    queue = Queue()
    n = int(input("Enter the number you want to stop at: "))
    queue.enqueue("1")
    for i in range(n):
        front = str(queue.dequeue())
        queue.enqueue(front + '0')
        queue.enqueue(front + '1')
        print(front)
    ''' WRITE YOUR CODE HERE '''
    ''' Ask the user for "n" '''
    ''' Use Queues in order to write the binary numbers from 1 to n '''
    ''' For example: if n = 5 output will be 1 10 11 100 101 '''

main()
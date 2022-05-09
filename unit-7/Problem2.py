from Queues import Queue


def ReverseNumber(number):
    # Step1: Create a result variable
    result = 0
    # Step2: Create an empty Queue
    myquue = Queue()
    while number != 0:
        myquue.enqueue(number % 10)
        number = round((number - number % 10) / 10)
    while not myquue.isEmpty():
        result += myquue.dequeue() * (10 ** myquue.getSize())
    return result
    '''
    1 - Create a result variable to hold the results - DONE FOR YOU
    2 - Create an empty Queue called myqueue - DONE FOR YOU
    3 - In Loop While the number is not 0:
        a) enqueue the remainder of the number divided by 10
        b) divide the number by 10
    4 - Loop over the queue "myqueue" and dequeue the elements into the result variable
    5 - return the result variable
    '''


    ##########################
    ### Write your code here
    ##########################


def main():
    mynumber = int(input("Enter a 7 digit number you need to reverse: "))
    print("The reversed number is: ", ReverseNumber(mynumber))


main()

# Name: Andrew Lee
# OSU Email: leea6@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 3
# Due Date: 10/31/2022
# Description: An implementation of a queue using linked lists. Included methods are enqueue, dequeue, and front



from SLNode import SLNode


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Queue:
    def __init__(self):
        """
        Initialize new queue with head and tail nodes
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = None
        self._tail = None

    def __str__(self):
        """
        Return content of queue in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'QUEUE ['
        if not self.is_empty():
            node = self._head
            out = out + str(node.value)
            node = node.next
            while node:
                out = out + ' -> ' + str(node.value)
                node = node.next
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the queue is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._head is None

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        node = self._head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    # -----------------------------------------------------------------------

    def enqueue(self, value: object) -> None:
        '''method adds given value to the back of the queue. Different cases depending on whether the head and/or tail
        is empty, and the case when both are already assigned to nodes. '''
        if self._head == None:
            self._head = SLNode(value)
        elif self._tail == None:
            self._tail = SLNode(value)
            self._head.next = self._tail
        else:
            new_node = SLNode(value)
            self._tail.next = new_node
            self._tail = new_node

    def dequeue(self) -> object:
        '''method removes the first element in the list and returns it. Raises an exception if the queue is empty'''
        if self.size() == 0:
            raise QueueException
        value_returned = self._head.value
        self._head = self._head.next
        return value_returned

    def front(self) -> object:
        '''method returns the first element in the list. Raises an exception if the queue is empty'''
        if self.size() == 0:
            raise QueueException
        return self._head.value


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# enqueue example 1")
    q = Queue()
    print(q)
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)

    print("\n# dequeue example 1")
    q = Queue()
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)
    for i in range(6):
        try:
            print(q.dequeue())
        except Exception as e:
            print("No elements in queue", type(e))

    print('\n#front example 1')
    q = Queue()
    print(q)
    for value in ['A', 'B', 'C', 'D']:
        try:
            print(q.front())
        except Exception as e:
            print("No elements in queue", type(e))
        q.enqueue(value)
    print(q)

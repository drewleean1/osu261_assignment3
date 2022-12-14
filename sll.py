# Name: Andrew Lee
# OSU Email: leea6@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 3
# Due Date: 10/31/2022
# Description: Implementing singly linked lists


from SLNode import *


class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class LinkedList:
    def __init__(self, start_list=None) -> None:
        """
        Initialize new linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = SLNode(None)

        # populate SLL with initial values (if provided)
        # before using this feature, implement insert_back() method
        if start_list is not None:
            for value in start_list:
                self.insert_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        node = self._head.next
        while node:
            out += str(node.value)
            if node.next:
                out += ' -> '
            node = node.next
        out += ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        node = self._head.next
        while node:
            length += 1
            node = node.next
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return not self._head.next

    # ------------------------------------------------------------------ #

    def insert_front(self, value: object) -> None:
        '''method adds given value to the front of the list '''
        new_node = SLNode(value, self._head.next)
        self._head = SLNode(None, new_node)

    def insert_back(self, value: object) -> None:
        '''method adds given value to the back of the list.'''
        current = self._head
        for x in range (self.length()):                 #for loop to iterate to back of the list
            current = current.next
        current.next = SLNode(value, None)


    def insert_at_index(self, index: int, value: object) -> None:
        '''method inserts given value at the given value. Raises an exception if the index is invalid.'''
        if index < 0 or index > self.length():
            raise SLLException
        current = self._head
        if index == 0:
            self.insert_front(value)
        else:
            for x in range (index):
                current = current.next
            new_node = SLNode(value, current.next)
            current.next = new_node


    def remove_at_index(self, index: int) -> None:
        '''method removes the value at the given index and raises an exception if the given index is invalid'''
        if index < 0 or index > self.length() -1:
            raise SLLException
        current = self._head
        for x in range(index):
            current = current.next
        current.next = current.next.next                            #'skip' over the node we wish to remove

    def remove(self, value: object) -> bool:
        '''method removes the first element of the given value in the list. Returns a bool based on whether or not we
        removed the element from the list'''
        before = self._head                                 #double pointers to keep track of where we are in the list
        current = self._head.next
        for x in range(self.length()):
            try:
            #try and except so that if we get an exception, we know we didn't find the given value
                if current.value == value:
                    before.next = current.next              #utilize our double pointers to skip the node we want removed
                    return True
                before = before.next
                current = current.next
            except:
                return False
        return False

    def count(self, value: object) -> int:
        '''method returns the total number of the given value in the list'''
        counts = 0
        current = self._head
        for x in range(self.length()+1):
            if current.value == value:
                counts += 1
            current = current.next
        return counts

    def find(self, value: object) -> bool:
        '''method returns a bool based on whether or not the given value is in the list'''
        current = self._head
        for x in range(self.length()+1):
            if current.value == value:
                return True
            current = current.next
        return False

    def slice(self, start_index: int, size: int) -> "LinkedList":
        '''method returns a new LinkedList of given size, starting from the given start_index. Returns an exception
        if the given slice based on start_index and size is invalid'''
        if start_index < 0 or start_index > self.length() - 1 or start_index + size > self.length() or size<0:
            raise SLLException
        current = self._head
        for x in range(start_index):                            #for loop to get to the start of the slice
            current = current.next
        new_list = LinkedList()
        current = current.next
        for x in range(size):                                   #add elements until we reach the size of our slice
            new_list.insert_back(current.value)
            current = current.next
        return new_list



if __name__ == "__main__":

    print("\n# insert_front example 1")
    test_case = ["A", "B", "C"]
    lst = LinkedList()
    for case in test_case:
        lst.insert_front(case)
        print(lst)

    print("\n# insert_back example 1")
    test_case = ["C", "B", "A"]
    lst = LinkedList()
    for case in test_case:
        lst.insert_back(case)
        print(lst)

    print("\n# insert_at_index example 1")
    lst = LinkedList()
    test_cases = [(0, "A"), (0, "B"), (1, "C"), (3, "D"), (-1, "E"), (5, "F")]
    for index, value in test_cases:
        print("Inserted", value, "at index", index, ": ", end="")
        try:
            lst.insert_at_index(index, value)
            print(lst)
        except Exception as e:
            print(type(e))

    print("\n# remove_at_index example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6])
    print(f"Initial LinkedList : {lst}")
    for index in [0, 2, 0, 2, 2, -2]:
        print("Removed at index", index, ": ", end="")
        try:
            lst.remove_at_index(index)
            print(lst)
        except Exception as e:
            print(type(e))

    print("\n# remove example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    for value in [7, 3, 3, 3, 3]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")
    print("\n# remove example 2")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    for value in [1, 2, 3, 1, 2, 3, 3, 2, 1]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")


    print("\n# count example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 2])
    print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))


    print("\n# find example 1")
    lst = LinkedList(["Waldo", "Clark Kent", "Homer", "Santa Claus"])
    print(lst)
    print(lst.find("Waldo"))
    print(lst.find("Superman"))
    print(lst.find("Santa Claus"))

    print("\n# slice example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = lst.slice(1, 3)
    print("Source:", lst)
    print("Start: 1 Size: 3 :", ll_slice)
    ll_slice.remove_at_index(0)
    print("Removed at index 0 :", ll_slice)

    print("\n# slice example 2")
    lst = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("Source:", lst)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Start:", index, "Size:", size, end="")
        try:
            print(" :", lst.slice(index, size))
        except:
            print(" : exception occurred.")


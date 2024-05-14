from collections.abc import Iterator
from typing import Any

class Node:
    def __init__(self, data:Any):
        """
        Create and initialize Node class instance.
        >>> Node(20)
        Node(20)
        >>> Node("Hello, world!")
        Node(Hello, world!)
        >>> Node(None)
        Node(None)
        >>> Node(True)
        Node(True)
        """

        self.data = data
        self.next = None

    def __repr__(self) -> str:
        """
        Get the string representation of this node.
        >>> Node(10).__repr__()
        'Node(10)'
        >>> repr(Node(10))
        'Node(10)'
        >>> str(Node(10))
        'Node(10)'
        >>> Node(10)
        Node(10)
        """
        return f"Node({self.data})"


class LinkedList:
    def __init__(self):
        """
        Create and initialize LinkedList class instance.
        >>> linked_list = LinkedList()
        >>> linked_list.head is None
        True
        """
        self.head = None

    def __iter__(self):
        """
        This function is intended for iterators to access
        and iterate through data inside linked list. This function 
        implements the iterator protocol to allow for iterating through 
        the linked list elements. yield node.data essentially acts as a 
        checkpoint within a generator function designed to iterate 
        over a linked list. It returns the data (node.data) from the 
        current node to the caller (e.g., the for loop). Pauses the 
        execution of the generator, allowing the loop to move on to 
        the next node for the next iteration.
        >>> linked_list = LinkedList()
        >>> linked_list.insert_tail("tail")
        >>> linked_list.insert_tail("tail_1")
        >>> linked_list.insert_tail("tail_2")
        >>> for node in linked_list: # __iter__ used here.
                node
        ...
        'tail'
        'tail_1'
        'tail_2'
        """
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __len__(self) -> int:
        """
        Return length of linked list i.e. number of nodes
        >>> linked_list = LinkedList()
        >>> len(linked_list)
        0
        >>> linked_list.insert_tail("tail")
        >>> len(linked_list)
        1
        >>> linked_list.insert_head("head")
        >>> len(linked_list)
        2
        >>> _ = linked_list.delete_tail()
        >>> len(linked_list)
        1
        >>> _ = linked_list.delete_head()
        >>> len(linked_list)
        0
        """
        return sum(1 for _ in self)

    def __repr__(self) -> str:
        """
        String representation/visualization of a Linked Lists
        >>> linked_list = LinkedList()
        >>> linked_list.insert_tail(1)
        >>> linked_list.insert_tail(3)
        >>> linked_list.__repr__()
        '1 -> 3'
        >>> repr(linked_list)
        '1 -> 3'
        >>> linked_list.insert_tail(5)
        >>> f"{linked_list}"
        '1 -> 3 -> 5'
         """
        return " -> ".join([str(item) for item in self])

    def __getitem__(self, index: int) -> Any:
        """
        This defines a special method called __getitem__  for LL class.
        This method is called whenever the square bracket notation []
        on an instance of the class is used.  if we have an object ll_object
        of this class, then ll_object[1] would be equivalent to calling ll_object.__getitem__(1).
        Provides Indexing Support. Used to get a node at particular position
        >>> linked_list = LinkedList()
        >>> for i in range(0, 10):
        ...     linked_list.insert_nth(i, i)
        >>> all(str(linked_list[i])) == str(i) for i in range(0, 10))
        True
        >>> linked_list[-10]
        Traceback (most recent call last):
            ...
        ValueError: list index out of range.
        """
        if not 0 <= index < len(self):
            raise ValueError("list index out of range.")
        for i, node in enumerate(self):
             if i == index:
                return node
        return None

    # Change the data of a particular node
    def __setitem__(self, index: int, data: Any) -> None:
        """
        >>> linked_list = LinkedList()
        >>> for i in range(0, 10):
        ...    linked_list.insert_nth(i, i)
        >>> linked_list[0] = 666
        >>> linked_list[0]
        666
        >>> linked_list[5] = -666
        >>> linked_list[5]
        -666
        >>> linked_list[5] = -666
        >>> linked_list[5]
        -666
        >>> linked_list[-10] = 666
        Traceback (most recent call last):
            ...
        ValueError: list index out of range.
        >>> linked_list[len(linked_list)] = 666
        Traceback (most recent call last):
            ...
        ValueError: list index out of range.
        >>> linked_list[len(linked_list)] = 666
        Traceback (most recent call last):
            ...
        ValueError: list index out of range.
        """
        if not 0 <= index < len(self):
            raise ValueError("list index out of range.")
        current = self.head
        for _ in range(index):
            current = current.next
        current.data = data

    def insert_tail(self, data: Any) -> None:
        """
        Insert data to the end of linked list.
        >>> linked_list = LinkedList()
        >>> linked_list.insert("tail")
        >>> linked_list
        tail
        >>> linked_list.insert_tail("tail_2")
        >>> linked_list
        tail -> tail_2
        >>> linked_list.insert_tail("tail_3")
        >>> tail_2 -> tail_3
        """
        self.insert_nth(len(self), data)

    def insert_nth(self, index: int, data: Any) -> None:
        """
        Insert data at given index.
        >>> linked_list = LinkedList()
        >>> linked_list.insert_tail("first")
        >>> linked_list.insert_tail("second")
        >>> linked_list.insert_tail("third")
        >>> linked_list
        first -> second -> third
        >>> linked_list.insert_nth(1, "fourth")
        >>> linked_list
        first -> fourth -> second -> third
        >>> linked_list.insert_nth(3,"fifth")
        >>> linked_list
        first -> fourth -> second -> fifth -> third
        """
        if not 0 <= index <= len(self):
            raise IndexError("list index out of range")
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        elif index == 0:
            new_node.next = self.head # link new_node to head
            self.head = new_node
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node

    def print_list(self) -> None:  # print every node data
        """
        This method prints every node data.
        >>> linked_list = LinkedList()
        >>> linked_list.insert_tail("first")
        >>> linked_list.insert_tail("second")
        >>> linked_list.insert_tail("third")
        >>> linked_list
        first -> second -> third
        """
        print(self)

    def delete_head(self) -> Any:
        """
        Implement This next
        """
        return

    def delete_nth(self, index: int = 0) -> Any:
        """
        Delete node at given index and return the
        node's data.
        >>> linked_list = LinkedList()
        >>> linked_list.insert_tail("first")
        >>> linked_list.insert_tail("second")
        >>> linked_list.insert_tail("third")
        >>> linked_list
        first -> second -> third
        >>> linked_list.delete_nth(1) # delete middle
        'second'
        >>> linked_list
        first -> third
        >>> linked_list.delete_nth(5) # this raises error
        Traceback (most recent call last):
            ...
        IndexError: List index out of range.
        >>> linked_list.delete_nth(-1) # this also raises error
        Traceback (most recent call last):
            ...
        IndexError: List index out of range.
        """
        if not 0 <= index <= len(self) - 1:
            raise IndexError("List index out of range.")
        delete_node = self.head

        if index == 0:
            self.head = self.head.next
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            delete_node = temp.next
            temp.next = temp.next.next
        return delete_node.data




    def is_empty(self) -> bool:
        """
        Check if linked list is empty.
        >>> linked_list = LinkedList()
        >>> linked_list.is_empty()
        True
        >>> linked_list.insert_head("first")
        >>> linked_list.is_empty()
        False
        """

        return self.head is None

    def reverse(self) -> None:
        """
        This reverses the linked list order.
        >>> linked_list = LinkedList()
        >>> linked_list.insert_tail("first")
        >>> linked_list.insert_tail("second")
        >>> linked_list.insert_tail("third")
        >>> linked_list
        first -> second -> third
        >>> linked_list.reverse()
        >>> linked_list
        third -> second -> first
        """
        prev = None
        current = self.head
        # 1 -> 2 -> 3 -> 4
        # next = 2
        #    1    2 -> 3 -> 4 -> 5
        #    ^    ^
        #    |    |
        #    prev current           ##End Iteration 1
        # next = 3
        #    1  <-  2   3 -> 4 -> 5
        #               ^    ^
        #               |    |
        #               prev current    ##End Iteration 2
        while current:
            # store the current node's next node
            next = current.next
            # make the current node's next node point backwards
            current.next = prev
            # make the previous node be the current node
            prev = current
            # make the current node the next node (to progress iteration)
            current = next
        self.head = prev



        

        



def main():

    linked_list = LinkedList()

if __name__ == "__main__":
    main()



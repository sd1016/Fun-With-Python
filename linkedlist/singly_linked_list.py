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
        """Implement this"""
        return        
    
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
            new_node.next_node = self.head # link new_node to head
            self.head = new_node
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next_node
            new_node.next_node = temp.next_node
            temp.next_node = new_node



        

        



def main():

    linked_list = LinkedList()

if __name__ == "__main__":
    main()



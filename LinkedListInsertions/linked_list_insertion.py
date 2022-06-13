class LinkedList:

    def __init__(self, head=None):
        """
        This is the constructor for the actual linked list.

        Arguments: head (optional param that defaults to none and represents the head of the linked list).
        """
        self.head = head

    def insert(self, value):
        """
        Insert a value to the head of the linked list.

        Arguments: value (value that the new node represents)
        """
        node = Node(value)

        if self.head is not None:
            node.next = self.head

        self.head = node

    def includes(self, value):
        """
        Search the linked list for a specific value.

        Arguments: value (value we are searching for in the list).

        Output: A boolean (true of false).
        """

        current = self.head

        while current is not None:
            if current.value == value:
                return True

            current = current.next

        return False

    def append(self, value):
        """
        Appends value to end of linked list
        Arguments: value (value we trying to append).
        """
        node = Node(value)
        current = self.head
        if self.head == None:
            self.head = node
            return

        while current.next is not None:
            current = current.next

        current.next = node

    def insertBefore(self, value, newVal):
        """
        Inserts value before a specified value
        Arguments: value and newVal (we are trying to insert newVal before value (if exists)).
        """
        current = self.head

        if current.value == value:
            self.insert(newVal)
            return

        while current is not None:
            if current.next.value == value:
                node = Node(newVal)
                node.next = current.next
                current.next = node
                return
            current = current.next

        raise Exception(f"{{{value}}} does not exist in the linked list!")

    def insertAfter(self, value, newVal):
        """
        Inserts value after a specified value
        Arguments: value and newVal (we are trying to insert newVal after value (if exists)).
        """
        current = self.head

        while current is not None:
            if current.value == value:
                node = Node(newVal)
                node.next = current.next
                current.next = node
                return
            current = current.next

        raise Exception(f"{{{value}}} does not exist in the linked list!")

    def __str__(self):
        """
        Produce a string representation of the linked list.

        Output: String representation of the linked list.
        """

        current = self.head
        string = ''

        while current is not None:
            string += f"{{{current.value}}}->"
            current = current.next

        return string + 'NULL'


class Node:

    def __init__(self, value, next=None):
        """
        This is the Node Constructor

        Arguments: value (value that the node represents) and next (optional param that defaults to none and represents the next node in the list).
        """
        self.value = value
        self.next = next

class Node:
    """
    It will store the data and the reference to the next node
    """

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """
    create a sequence of Nodes
    """

    def __init__(self):
        self.head = None

    def insert(self, value):
        """
        insert value into LinkedList as node
        """
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            self.head = node
            self.head.next = current

    def includes(self, key):
        search_element = Node(key)
        current = self.head
        while current:
            if current.value == search_element.value:
                return True
            current = current.next
        return False

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            current = self.head

            while current.next:
                current = current.next

            current.next = node

    def insert_before(self, value, new_value):
        node = Node(new_value)
        if self.head.value == value:
            node.next = self.head
            self.head = node
        else:
            current = self.head
            while current.next:
                if current.next.value == value:
                    node.next = current.next
                    current.next = node
                    break

                current = current.next
            if current.next is None:
                raise ValueError(f'node with value {value} it is not founded')

    def insert_after(self, value, new_value):
        node = Node(new_value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current:
                if current.value == value:
                    node.next = current.next
                    current.next = node
                    break
                current = current.next

            if current is None:
                raise ValueError(f'node with value {value} it is not founded')

    def kth_from_end(self, k):
        if k < 0:
            return 'your input should be positive value'
        else:
            if self.head is None:
                return 'Empty linked list'
            else:
                length = 0
                current = self.head
                while current:
                    current = current.next
                    length += 1
                if length - 1 < k:
                    return 'your input is greater than the length of the list'
                else:
                    location = length - k
                    current = self.head
                    for pointer in range(location-1):
                        current = current.next
                    return current.value

    def to_string(self):
        """
        to  represent all the values in the Linked List, formatted
        """
        current = self.head
        formatting = ''
        opening = '{'
        closing = '}'
        while current:
            formatting += f'{opening}{current.value}{closing} -> '
            current = current.next
        formatting += 'NULL'
        return formatting

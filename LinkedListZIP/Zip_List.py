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

def zipLists(list1, list2):
    # Start pointing the nodes
    curr1 = list1.head
    curr2 = list2.head
    while curr1 != None and curr2 != None:
        next1 = curr1.next
        next2 = curr2.next
        curr2.next = next1
        curr1.next = curr2
        curr1 = next1
        curr2 = next2
        list2.head = curr2
    #Handle the case where list1 become empty before list2
    if curr2:
        list1.Append(curr2.data)
    return list1.ToString()


if __name__ == '__main__':
    list1 = LinkedList()
    list1.append(1)
    list1.append(3)
    list1.append(2)

    list2 = LinkedList()
    list2.append(5)
    # list2.Append(9)
    # list2.Append(4)

    list1.to_string()
    print()
    list2.to_string()
    print()

    zipLists(list1,list2)
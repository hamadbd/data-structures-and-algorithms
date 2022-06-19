import pytest
from KTH_linked_list import LinkedList, Node


def test_Nodes(node):
    """
    test if the Node created successfully
    """
    assert node


def test_empty_linked_list_creation(linked_list):
    """
    test successfully instantiate an empty linked list
    """
    assert linked_list


def test_insert__SingleNodes_into_linked_list(linked_list):
    """
    test insert single value into linked_list successfully
    """
    linked_list.insert(1)
    actual = linked_list.to_string()
    expected = '{1} -> {3} -> {2} -> {1} -> NULL'
    assert actual == expected


def test_insert__multipleNodes_into_linked_list(linked_list):
    """
    test insert single value into linked_list successfully
    """
    linked_list.insert(4)
    linked_list.insert(5)
    linked_list.insert(6)
    actual = linked_list.to_string()
    expected = '{6} -> {5} -> {4} -> {3} -> {2} -> {1} -> NULL'
    assert actual == expected


def test_Head(linked_list):
    """
    test if the head points to the first node in the linked list
    """
    linked_list.insert(7)
    actual = linked_list.head.value
    expected = 7
    assert actual == expected
    # assert linked_list.head.value


def test_includes_exists_value(linked_list):
    """
    test search values in linked_list will return True if it exists
    """
    actual = linked_list.includes(2)
    expected = True
    assert actual == expected


def test_includes_Not_exists_value(linked_list):
    """
    test search values in linked_list will return False if it does not exist
    """
    actual = linked_list.includes(100)
    expected = False
    assert actual == expected


def test_append_to_linked_list(a_linked_list):
    """
    to add a node to the end of the linked list
    """
    a_linked_list.append(5)
    actual = a_linked_list.to_string()
    expected = '{1} -> {3} -> {2} -> {5} -> NULL'
    assert actual == expected


def test_append_Multi_Node_to_linked_list(a_linked_list):
    """
    to add multiple nodes to the end of the linked list
    """
    a_linked_list.append(5)
    a_linked_list.append(6)
    a_linked_list.append(7)
    actual = a_linked_list.to_string()
    expected = '{1} -> {3} -> {2} -> {5} -> {6} -> {7} -> NULL'
    assert actual == expected


def test_insert_before_middle_to_linked_list(i_linked_list):
    """
    to  insert a node before a node located i the middle of a linked list
    """
    i_linked_list.insert_before(3, 5)
    actual = i_linked_list.to_string()
    expected = '{1} -> {5} -> {3} -> {2} -> NULL'
    assert actual == expected


def test_insert_before_first_to_linked_list(i_linked_list):
    """
    to insert a node before the first node of a linked list
    """
    i_linked_list.insert_before(1, 5)
    actual = i_linked_list.to_string()
    expected = '{5} -> {1} -> {3} -> {2} -> NULL'
    assert actual == expected


def test_insert_before_to_linked_list(ll):
    """
    to insert before the first {2} in the linked_list
    """
    ll.insert_before(2, 5)
    actual = ll.to_string()
    expected = '{1} -> {5} -> {2} -> {2} -> NULL'
    assert actual == expected


def test_insert_before_not_existing_Node_to_linked_list(i_linked_list):
    """
    to raise value error when insert before not existing Node
    """
    try:
        i_linked_list.insert_before(4, 5)
    except ValueError:
        return ValueError == 'node with value 4 it is not founded'


def test_insert_after_middle_to_linked_list(i_linked_list):
    """
    to insert after a node in the middle of the linked list
    """
    i_linked_list.insert_after(3, 5)
    actual = i_linked_list.to_string()
    expected = '{1} -> {3} -> {5} -> {2} -> NULL'
    assert actual == expected


def test_insert_after_the_end_to_linked_list(i_linked_list):
    """
    to insert a node after the last node of the linked list
    """
    i_linked_list.insert_after(2, 5)
    actual = i_linked_list.to_string()
    expected = '{1} -> {3} -> {2} -> {5} -> NULL'
    assert actual == expected


def test_insert_after_to_linked_list(ll):
    """
    to insert after the first {2} in the linked_list
    """
    ll.insert_after(2, 5)
    actual = ll.to_string()
    expected = '{1} -> {2} -> {5} -> {2} -> NULL'
    assert actual == expected


def test_insert_after_not_existing_Node_to_linked_list(i_linked_list):
    """
    to raise value error when insert after not existing Node
    """
    try:
        i_linked_list.insert_after(4, 5)
    except ValueError:
        return ValueError == 'node with value 4 it is not founded'


def test_kth_from_end_Where_k_is_greater_than_the_length_of_the_linked_list(k_linked_list):
    actual = k_linked_list.kth_from_end(15)
    expected = 'your input is greater than the length of the list'
    assert actual == expected


def test_kth_from_end_Where_k_and_the_length_of_the_list_are_the_same(k_linked_list):
    actual = k_linked_list.kth_from_end(1)
    expected = 20
    assert actual == expected


def test_kth_from_end_Where_k_is_not_a_positive_integer(k_linked_list):
    actual = k_linked_list.kth_from_end(-5)
    expected = 'your input should be positive value'
    assert actual == expected


def test_kth_from_end_Where_the_linked_list_is_of_a_size_one(k_linked_list):
    new_linked_list = LinkedList()
    new_linked_list.insert(30)
    # the size of new_linked_list is one
    actual = new_linked_list.kth_from_end(0)
    expected = 30
    assert actual == expected


def test_kth_from_end(k_linked_list):
    actual = k_linked_list.kth_from_end(1)
    expected = 20
    assert actual == expected


def test_to_string(linked_list):
    """
    test represent the linked list values in a formatted way
    """
    actual = linked_list.to_string()
    expected = '{3} -> {2} -> {1} -> NULL'
    assert actual == expected


##############
# pytest.fixture
##############

# create Node
@pytest.fixture
def node():
    node = Node(5)
    return node


# create linked_list
@pytest.fixture
def linked_list():
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    return linked_list


@pytest.fixture
def a_linked_list():
    a_linked_list = LinkedList()
    a_linked_list.append(1)
    a_linked_list.append(3)
    a_linked_list.append(2)
    return a_linked_list


@pytest.fixture
def i_linked_list():
    i_linked_list = LinkedList()
    i_linked_list.append(1)
    i_linked_list.append(3)
    i_linked_list.append(2)
    return i_linked_list


@pytest.fixture
def ll():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(2)
    return ll


@pytest.fixture
def k_linked_list():
    k_l = LinkedList()
    k_l.insert(10)
    k_l.insert(20)
    return k_l
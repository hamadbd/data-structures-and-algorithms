import pytest
from linked_list_insertion import LinkedList, Node


def test_import():
    assert LinkedList

# Test empty list
def test_empty_list():
    actual = LinkedList().head
    expected = None
    assert actual == expected

# Test inserting node into list
def test_insert_in_list():
    link_list = LinkedList()
    link_list.insert(75)
    actual = link_list.head.value
    expected = 75
    assert actual == expected

# Testing True for includes
def test_list_includes_one():
    node = Node(100)
    actual = LinkedList(node).includes(100)
    expected = True
    assert actual == expected

# Testing head points (->) to first node
def test_list_head():
    node = Node(45)
    actual = LinkedList(node).head
    expected = node
    assert actual == expected

# Testing inserting multiple nodes
def test_insert_multiple_nodes():
    val1 = 'Trump'
    val2 = 'Melania'
    val3 = 'Conway'
    val4 = 'Huckabee'
    linked_list = LinkedList(val1)
    linked_list.insert(val2)
    linked_list.insert(val3)
    linked_list.insert(val4)
    actual = linked_list.head.value
    expected = 'Huckabee'
    assert actual == expected

# Testing False for includes
def test_if_list_includes_two():
    node = Node(50)
    actual = LinkedList(node).includes(49)
    expected = False
    assert actual == expected

# Testing the string method
def test_linked_list_str():
    link_list = LinkedList()
    link_list.insert('c')
    link_list.insert('b')
    link_list.insert('a')
    actual = str(link_list)
    expected = "{a}->{b}->{c}->NULL"
    assert actual == expected

# Add node to end of list
def test_append_node_to_list():
    link_list = LinkedList()
    link_list.insert('b')
    link_list.insert('c')
    link_list.append('a')
    actual = str(link_list)
    expected = "{c}->{b}->{a}->NULL"
    assert actual == expected

# Add multiple nodes to end of list
def test_append_nodes_to_list():
    link_list = LinkedList()
    link_list.insert('c')
    link_list.insert('d')
    link_list.append('b')
    link_list.append('a')
    actual = str(link_list)
    expected = "{d}->{c}->{b}->{a}->NULL"
    assert actual == expected

# insert before middle
def test_insert_before_middle():
    link_list = LinkedList()
    link_list.insert('c')
    link_list.insert('d')
    link_list.append('b')
    link_list.append('a')
    link_list.insertBefore('b', 'yasss')
    actual = str(link_list)
    expected = "{d}->{c}->{yasss}->{b}->{a}->NULL"
    assert actual == expected

# insert before first
def test_insert_before_first():
    link_list = LinkedList()
    link_list.insert('c')
    link_list.insert('d')
    link_list.append('b')
    link_list.append('a')
    link_list.insertBefore('d', 'yasss')
    actual = str(link_list)
    expected = "{yasss}->{d}->{c}->{b}->{a}->NULL"
    assert actual == expected

# insert after middle
def test_insert_after_middle():
    link_list = LinkedList()
    link_list.insert('c')
    link_list.insert('d')
    link_list.append('b')
    link_list.append('a')
    link_list.insertAfter('c', 'yasss')
    actual = str(link_list)
    expected = "{d}->{c}->{yasss}->{b}->{a}->NULL"
    assert actual == expected

# insert after last
def test_insert_after_last():
    link_list = LinkedList()
    link_list.insert('c')
    link_list.insert('d')
    link_list.append('b')
    link_list.append('a')
    link_list.insertAfter('a', 'yasss')
    actual = str(link_list)
    expected = "{d}->{c}->{b}->{a}->{yasss}->NULL"
    assert actual == expected
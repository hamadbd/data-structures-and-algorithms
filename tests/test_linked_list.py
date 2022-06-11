import pytest
from LinkedList.linkedlist import (
Node,
LinkedList
)


def test_head_node(data_head):
    actual = data_head
    expected = 25
    assert actual == expected

def test_not_include(not_include):
    actual = not_include
    expected = False
    assert actual == expected


def test_empty_list():
    testing =  LinkedList()
    actual = str(testing.ToString())
    expected = 'The list is empty.'
    assert actual == expected


def test_insert(data_testing_list):
    actual = data_testing_list
    expected = [10]
    assert actual == expected


def test_insert_multiple(data_testing_insertion):
    actual = data_testing_insertion
    expected =[25,20,15,10]
    assert actual == expected

#
def test_includes(include):
    actual = include
    expected = True
    assert actual == expected


@pytest.fixture()
def data_testing_list():
    testing = LinkedList()
    testing.Insert(10)
    return testing.ToString()

@pytest.fixture()
def data_testing_insertion():
    testing = LinkedList()
    testing.Insert(10)
    testing.Insert(15)
    testing.Insert(20)
    testing.Insert(25)
    return testing.ToString()

@pytest.fixture()
def data_head():
    testing = LinkedList()
    testing.Insert(10)
    testing.Insert(15)
    testing.Insert(20)
    testing.Insert(25)
    return testing.head.data

@pytest.fixture()
def include():
    testing = LinkedList()
    testing.Insert(10)
    testing.Insert(15)
    testing.Insert(20)
    testing.Insert(25)
    return testing.Includes(10)

@pytest.fixture()
def not_include():
    testing = LinkedList()
    testing.Insert(10)
    testing.Insert(15)
    testing.Insert(20)
    testing.Insert(25)
    return testing.Includes(30)
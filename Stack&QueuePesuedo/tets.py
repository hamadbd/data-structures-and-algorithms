import pytest

from stack_and_queue import *

def test_instantiate_empty_stack():
    """
    Can successfully instantiate an empty stack
    """
    stack = Stack()
    actual = stack.top
    expected = None
    assert actual == expected


def test_push_stack(stack):
    """
    Can successfully push onto a stack
    """
    stack.push(4)
    actual = stack.top.value
    expected = 4
    assert actual == expected


def test_push_multiple_values_stack(stack):
    """
    Can successfully push multiple values onto a stack
    """
    stack.push(5)
    stack.push(6)
    stack.push(7)
    actual = stack.top.value
    expected = 7
    assert actual == expected


def test_pop_stack(stack):
    """
    Can successfully pop off the stack
    """
    stack.pop()
    actual = stack.top.value
    expected = 2
    assert actual == expected


def test_multiple_pop_stack(stack):
    """
    Can successfully empty a stack after multiple pops
    """
    stack.pop()
    stack.pop()
    stack.pop()
    actual = stack.top
    expected = None
    assert actual == expected


def test_peek_stack(stack):
    """
    Can successfully peek the next item on the stack
    """
    stack.peek()
    actual = stack.top.value
    expected = 3
    assert actual == expected


def test_stack_raises_exception_pop():
    """
    Calling pop on empty stack raises exception
    """
    stack = Stack()
    with pytest.raises(EmptyStackException):
        stack.pop()


def test_stack_raises_exception_peek():
    """
    Calling peek on empty stack raises exception
    """
    stack = Stack()
    with pytest.raises(EmptyStackException):
        stack.peek()


#########################################################
##                  Queue TESTS                       ###
#########################################################


def test_instantiate_empty_queue():
    """
    Can successfully instantiate an empty queue
    """
    queue = Queue()
    actual = queue.front
    expected = None
    assert actual == expected


def test_enqueue_queue(queue):
    """
    Can successfully enqueue into a queue
    """
    queue.enqueue(4)
    actual = queue.rear.value
    expected = 4
    assert actual == expected


def test_enqueue_multiple_values_queue(queue):
    """
    Can successfully enqueue multiple values into a queue
    """
    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(7)
    actual = queue.rear.value
    expected = 7
    assert actual == expected


def test_dequeue_queue(queue):
    """
    Can successfully dequeue out of a queue the expected value
    """
    queue.dequeue()
    actual = queue.front.value
    expected = 2
    assert actual == expected


def test_multiple_dequeue_queue(queue):
    """
    Can successfully empty a queue after multiple dequeues
    """
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()

    actual = queue.front
    expected = None
    assert actual == expected


def test_peek_queue(queue):
    """
    Can successfully peek into a queue, seeing the expected value
    """
    queue.peek()
    actual = queue.front.value
    expected = 1
    assert actual == expected


def test_queue_raises_exception_dequeue():
    """
    Calling dequeue on empty queue raises exception
    """
    queue = Queue()
    with pytest.raises(EmptyQueueException):
        queue.dequeue()


def test_queue_raises_exception_peek():
    """
    Calling peek on empty queue raises exception
    """
    queue = Queue()
    with pytest.raises(EmptyQueueException):
        queue.peek()


##############
# fixture
##############

@pytest.fixture
def stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    return stack


@pytest.fixture
def queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    return queue
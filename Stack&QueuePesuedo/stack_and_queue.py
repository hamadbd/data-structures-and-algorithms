class EmptyStackException(Exception):
    pass


class EmptyQueueException(Exception):
    pass


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.is_empty():
            raise EmptyStackException('THIS STACK IS EMPTY')
        else:
            pooped = self.top
            self.top = self.top.next
        return pooped.value

    def is_empty(self):
        return True if self.top is None else False

    def peek(self):
        if self.is_empty():
            raise EmptyStackException('THIS STACK IS EMPTY')
        else:
            return self.top.value

    def __str__(self):
        current = self.top
        result = ''
        while current:
            result += str(current.value) + '\n'
            current = current.next
        return result


###########################################################


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = Node(value)
        if self.is_empty():
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueException('THIS QUEUE IS EMPTY')
        else:
            dequeued = self.front
            self.front = self.front.next
        return dequeued.value

    def is_empty(self):
        return True if self.front is None else False

    def peek(self):

        if self.is_empty():
            raise EmptyQueueException('THIS QUEUE IS EMPTY')
        else:
            return self.front.value

    def __str__(self):
        current = self.front
        result = ''
        while current:
            result += str(current.value) + '\t'
            current = current.next
        return result


###########################################################


if __name__ == '__main__':

    stack = Stack()
    stack.push(0)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    print(stack)


    queue = Queue()
    queue.enqueue(0)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)

    print(queue)

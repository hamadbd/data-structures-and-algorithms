class EmptyStackException(Exception):
    pass


class EmptyQueueException(Exception):
    pass


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

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

class AnimalShelter:
    def __init__(self):
        self.cats = Queue()
        self.dogs = Queue()

    def enqueue(self, animal):
        if animal.type == 'Dog':
            self.dogs.enqueue(animal)
        elif animal.type == 'Cat':
            self.cats.enqueue(animal)

    def dequeue(self, pref):
        if pref == 'dog':
            return self.dogs.dequeue()
        elif pref == 'cat':
            return self.cats.dequeue()
        else:
            return None


class Dog:
    def __init__(self, name):
        self.type = 'Dog'
        self.name = name


class Cat:
    def __init__(self, name):
        self.type = 'Cat'
        self.name = name


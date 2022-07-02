# Stacks and Queues 
- A stack is a conceptual structure consisting of a set of homogeneous elements and is based on the principle of last in first out (LIFO). It is a commonly used abstract data type with two major operations, namely push and pop. Push and pop are carried out on the topmost element, which is the item most recently added to the stack. The push operation adds an element to the stack while the pop operation removes an element from the top position. The stack concept is used in programming and memory organization in computers
- A Queue is a linear structure which follows a particular order in which the operations are performed. The order is First In First Out (FIFO). A good example of a queue is any queue of consumers for a resource where the consumer that came first is served first. The difference between stacks and queues is in removing. In a stack we remove the item the most recently added; in a queue, we remove the item the least recently added.

## Challenge
Using a Linked List as the underlying data storage mechanism, implement both a Stack and a Queue

### Approach & Efficiency
- Stack and Queue Logic


- Big O for stack Implementation 
  - Time 
    - push 0(1)
    - pop 0(1)
    - is_empty O(1)
    - peek 0(1)
    - Dunder str O(n) n equal the length of the stack
  - Space : 
    - push 0(1)
    - pop 0(1)
    - is_empty O(1)
    - peek 0(1)


- Big O for queue Implementation 
  - Time 
    - enqueue 0(1)
    - dequeue 0(1)
    - is_empty O(1)
    - peek 0(1)
    - Dunder str O(n) n equal the length of the queue
  - Space : 
    - enqueue 0(1)
    - dequeue 0(1)
    - is_empty O(1)
    - peek 0(1)




##### API


- push : create new node with the value and make the next of the node equal the top and the top equal the node
- pop : check if the stack is empty, if yes raise error, if no top equal the next of the top 
- peek : check if the stack is empty, if yes raise error, if no return the top 
- is_empty : check if the top is None, if yes return True which is empty stack, if no return False which is not empty stack
- enqueue : create new node with the value and check if the queue is empty, if yes the front equal node and the rear equal node , if no the next of the rear equal node, and rear equal node
- dequeue : check if the queue is empty, if yes raise error, if no the front equal the next of the front 
- is_empty : check if the front is None, if yes return True which is empty queue, if no return False which is not empty queue
- peek :check if the queue is empty, if yes raise error, if no return the front

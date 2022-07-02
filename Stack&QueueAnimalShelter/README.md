# AnimalShelter
Create a class called AnimalShelter which holds only dogs and cats.
The shelter operates using a first-in, first-out approach.
Implement the following methods:
enqueue
Arguments: animal
animal can be either a dog or a cat object.
dequeue
Arguments: pref
pref can be either "dog" or "cat"
Return: either a dog or a cat, based on preference.
If pref is not "dog" or "cat" then return null.

## Whiteboard
![image](Untitled%20(5).jpg)


## Approach & Efficiency
- Big O 
  - Time complexity: O(1)
  - Space complexity: O(1)
- I used two queues 
  - dogs queue to enqueue the dogs objects 
  - cats queue to enqueue the cats objects 
  - enqueue and dequeue methods 

  
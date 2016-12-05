###############################################################################
#
# 3.6 Animal Shelter
#
# An animal shelter, which holds only dogs and cats, operates on a strictly
# "first in, first out" basis. People must adopt either the "oldest" (based on
# arrival time) of all animals at the shelter, or they can select whether they
# would prefer a dog or a cat (and will receive the oldest animal of that
# type). They cannot select which specific animal they would like. Create the
# data structures to maintain this system and implement operations such as
# enqueue, dequeueAny, dequeueDog, and dequeueCat. You may use the built-in
# LinkedList data structure.
#
###############################################################################

import copy
import LibraryPath
from lib.LinkedList import LinkedList


class Animal:
    def __init__(self, animal_type):
        self.type = animal_type


class Shelter:
    def __init__(self):
        self.shelter = LinkedList()

    def enqueue(self, animal_type):
        animal = Animal(animal_type)
        self.shelter.add_node(animal)

    def dequeueAny(self):
        head = self.shelter.head
        if head is None:
            return None
        new_head = head.next
        self.shelter.head = new_head
        return head

    def _dequeueAnimal(self, animal_type):
        node = self.shelter.head
        while node.data.type != animal_type and node.next is not None:
            node = node.next

        if node.data.type != animal_type:
            return None
        else:
            animal = copy.deepcopy(node)
            if node.next is not None:
                node.data = node.next.data
                node.next = node.next.next
            return animal

    def dequeueCat(self):
        return self._dequeueAnimal('cat')

    def dequeueDog(self):
        return self._dequeueAnimal('dog')


s = Shelter()
s.enqueue('cat')
s.enqueue('dog')
s.enqueue('dog')
s.enqueue('cat')
s.enqueue('cat')
s.enqueue('dog')

print s.dequeueDog().data.type
print s.dequeueDog().data.type
print s.dequeueAny().data.type
print s.dequeueCat().data.type
print s.dequeueDog().data.type

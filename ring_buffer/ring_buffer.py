
from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('./doubly_linked_list')


class RingBuffer:
    def __init__(self, capacity):
        # Allows us to move through the indexs
        self.movingIndex = None
        self.storage = DoublyLinkedList()
        self.capacity = capacity

    def append(self, item):
        # on our first one we will add to tail and set our most recently used
        if self.storage.length == 0:
            self.storage.add_to_tail(item)
            self.movingIndex = self.storage.tail
            return

        # It being a ring we need to close our circle if we hit cap
        if self.storage.length == self.capacity:
            self.storage.tail.next = self.storage.head

        # Open Loop
        if self.storage.tail.next is None:
            self.storage.add_to_tail(item)
            self.movingIndex = self.movingIndex.next

        # Closed loop, start cycling the values
        else:
            self.movingIndex = self.movingIndex.next
            self.movingIndex.value = item

    def get(self):
        # Beacuse its a ring we need to start with the node past the head to know when to stop
        current_node = self.storage.head.next

        # add the starting node to the list
        storage_contents = [self.storage.head.value]

        # hitting head would mean we have completed our loop
        while current_node is not self.storage.head:

            # If loop isn't close we need to check
            if current_node is None:
                break
            storage_contents.append(current_node.value)
            current_node = current_node.next
        return storage_contents

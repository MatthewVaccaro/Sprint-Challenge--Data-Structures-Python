"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        newNode = ListNode(value)
        # None
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
            self.length += 1
            return value
        # One + Bunch
        else:
            # Assign Vars
            oldHead = self.head
            # OldHead Prev Value
            oldHead.prev = newNode
            # Assign New Head
            self.head = newNode
            # Assign New Head Next Value
            newNode.next = oldHead
            # Inc
            self.length += 1
            return value

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        removedHead = self.head
        # None
        if self.length == 0:
            return None
        # One
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
            return removedHead.value
        # Sum
        else:
            self.head = removedHead.next
            removedHead.next = None
            self.length -= 1
            return removedHead.value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        newNode = ListNode(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
            self.length += 1
            return value
        else:
            oldTail = self.tail
            oldTail.next = newNode
            self.tail = newNode
            newNode.prev = oldTail
            self.length += 1
            return value

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        removedTail = self.tail

        if self.length == 0:
            return None
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
            return removedTail.value
        else:
            newTail = removedTail.prev
            self.tail = newTail
            newTail.next = None
            removedTail.prev = None
            self.length -= 1
            return removedTail.value

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        if self.length == 0:
            return None
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
            return node.value
        elif node.next == None:  # Is this the tail?
            self.remove_from_tail()
        elif node.prev == None:  # is this the head?
            self.remove_from_head()
        else:
            # [ 9, "1", 6]
            # Assign vars to Next and Prev
            nextInList = node.next  # = 6
            prevInList = node.prev  # = 9
            # Assgin them to each other
            nextInList.prev = prevInList
            prevInList.next = nextInList
            # Remove Node
            node.next = None
            node.prev = None
            # Dec Length
            self.length -= 1

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node.value)

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.value)

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        currentNode = self.head  # Will hold the looping node
        maxValue = 0
        inc = 0
        if self.length == 0:
            return None
        elif self.tail == self.head:
            return self.head.value
        else:
            while inc is not self.length:
                if currentNode.value > maxValue:
                    maxValue = currentNode.value
                    currentNode = currentNode.next
                    inc += 1
                else:
                    currentNode = currentNode.next
                    inc += 1

        return maxValue

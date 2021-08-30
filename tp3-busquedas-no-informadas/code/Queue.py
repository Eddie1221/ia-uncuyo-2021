class node:
    value = None
    nextNode = None

class Queue:
    head = None
    tail = None

    def push(self,element):
        NewNode = node()
        NewNode.nextNode = self.head
        NewNode.value = element
        self.head = NewNode

    def enqueue(self,element):
        NewNode = node()
        NewNode.value = element
        if self.head != None:
            self.tail.nextNode = NewNode
            self.tail = NewNode
        else:
            self.head = NewNode
            self.tail = NewNode

    def dequeue(self):
        if self.head != None:
            nodo = self.head
            self.head = nodo.nextNode
            return nodo.value
        else:
            return None
class PriorityNode:
	value=None
	nextNode=None
	priority=None

class PriorityQueue:
  head=None
  tail=None

  def enqueue(self,element,priority):
      NewNode = PriorityNode()
      NewNode.value = element
      NewNode.priority = priority
      if self.head != None:
          if NewNode.priority >= self.tail.priority:
            self.tail.nextNode = NewNode
            self.tail = NewNode
          else:
            node = self.head
            while node.priority < NewNode.priority and node.nextNode != None:
              node = node.nextNode

            NewNode.nextNode = node.nextNode
            node.nextNode = NewNode

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
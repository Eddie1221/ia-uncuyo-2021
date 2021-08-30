class PriorityNode:

  def __init__(self, value, priority):
    self.value = value
    self.priority = priority


def enqueue(Lista, value, priority):
  newnode = PriorityNode(value, priority)

  for i in range(len(Lista)):
    if Lista[i].priority > newnode.priority:
      Lista.insert(i,newnode)
      return 

  Lista.append(newnode)

def dequeue(Lista):
  value = Lista[0].value
  Lista.pop(0)
  return value
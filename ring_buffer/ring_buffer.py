class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity
    self.container = []
    self.counter = 0

  def append(self, item):
    if self.counter < self.capacity:
      self.container.append(item)
      self.counter += 1
      print(self.container)
    else:
      if self.current == self.capacity:
        self.current = 0
      else:
        self.container[self.current] = item
        self.current += 1
        print(self.container)

  def get(self):
    return self.container
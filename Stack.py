#PUSH into a Stack
#Last in First Out(LIFO)
class Stack:
   def __init__(self):
      self.stack = []

   def add(self, value):
      if value not in self.stack:
         self.stack.append(value)
         return True
      else:
         return False
# Use peek to look at the top of the stack
   def peek(self):     
	   return self.stack[-1]

AStack = Stack()
AStack.add("Mon")
AStack.add("Tue")
AStack.peek()
print(AStack.peek())
AStack.add("Wed")
AStack.add("Thu")
print(AStack.peek())
'''**************************************************************************'''
#POP from a Stack
class Stack:
   def __init__(self):
      self.stack = []

   def add(self, value):
      if value not in self.stack:
         self.stack.append(value)
         return True
      else:
         return False
        
# Use list pop method to remove element
   def remove(self):
      if len(self.stack) <= 0:
         return ("No element in the Stack")
      else:
         return self.stack.pop()

AStack = Stack()
AStack.add("Mon")
AStack.add("Tue")
AStack.add("Wed")
AStack.add("Thu")
print(AStack.remove())
print(AStack.remove())
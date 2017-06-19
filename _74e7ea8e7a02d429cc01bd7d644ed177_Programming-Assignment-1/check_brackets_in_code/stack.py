class Stack:
	def __init__(self):
		self.items = []

	def push(self,e):
		self.items.append(e)

	def pop(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

	def peek(self):
		return self.items[0]
	


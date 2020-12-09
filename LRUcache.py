class node:
	def __init__(self, key, val):
		self.prev = None
		self.next = None
		self.key = key
		self.val = val

class LRUcache:
	def __init__(self, n):
		self.LRU_size = n
		self.h = {}
		self.start = None
		self.end = None

	def removeNode(self, entry):
		if entry.prev:
			entry.prev.next = entry.next
		else:
			self.start = entry.next

		if entry.next:
			entry.next.prev = entry.prev
		else:
			self.end = entry.prev

	def addAtTop(self, entry):
		entry.next = self.start
		if self.start:
			self.start.prev = entry
		self.start = entry
		if not self.end:
			self.end = self.start

	def get(self, key):
		if key in self.h:
			entry = self.h[key]
			self.removeNode(entry)
			self.addAtTop(entry)
			return entry.val

		return -1

	def put(self, key, val):		
		entry = node(key, val)
		if len(self.h) < self.LRU_size:
			self.addAtTop(entry)

		else:
			del self.h[self.end.key]
			self.removeNode(self.end)
			self.addAtTop(entry)

		self.h[key] = entry

obj = LRUcache(3)
obj.put(1, "a")
obj.put(2, "b")
obj.put(3, "c")
obj.put(4, "d")
print(obj.get(3))
print(obj.start.val, obj.start.next.val, obj.start.next.next.val)
class intSet(object):
	def __init__(self):
        	"""Create an empty set of integers"""
        	self.vals = []
	def insert(self, e):
	        """Assumes e is an integer and inserts e into self""" 
	        if not e in self.vals:
	            self.vals.append(e)
	def member(self, e):
	        """Assumes e is an integer
	           Returns True if e is in self, and False otherwise"""
	        return e in self.vals
	def remove(self, e):
	        """Assumes e is an integer and removes e from self
	           Raises ValueError if e is not in self"""
	        try:
	            self.vals.remove(e)
	        except:
	            raise ValueError(str(e) + ' not found')
	def __str__(self):
	        """Returns a string representation of self"""
	        self.vals.sort()
	        return '{' + ','.join([str(e) for e in self.vals]) + '}'
	def intersect(self,obj):
		new1=intSet()
		for i in self.vals:
			if obj.member(i):
				new1.insert(i)
		return new1
	def __len__(self):
		return len(self.vals)

n1=intSet()
n1.insert(2)
n1.insert(3)
n2=intSet()
n2.insert(3)
n3=n1.intersect(n2)
print(len(n3))

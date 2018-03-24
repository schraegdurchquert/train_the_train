class mappix:
	is_rail = False;
	r	= 0;
	g	= 0;
	b	= 0;

	def __init__(self,r,g,b):
		self.r = r
		self.g = g
		self.b = b

	def col(self):
		return(self.r,self.g,self.b)

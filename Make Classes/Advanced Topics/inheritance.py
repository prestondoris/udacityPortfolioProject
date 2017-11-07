class Parent():
	def __init__(self, last_name, eye_color):
		print("Parent Constructor Called")
		self.last_name = last_name
		self.eye_color = eye_color

class Child(Parent):
	def __init__(self, last_name, eye_color, num_toys):
		Parent.__init__(self, last_name, eye_color)
		self.num_toys = num_toys
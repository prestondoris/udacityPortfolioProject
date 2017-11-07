class Parent():
	def __init__(self, last_name, eye_color):
		print("Parent Constructor Called")
		self.last_name = last_name
		self.eye_color = eye_color

class Child(Parent):
	def __init__(self, last_name, eye_color, num_toys):
		print("Child Constructor Called")
		Parent.__init__(self, last_name, eye_color)
		self.num_toys = num_toys


#jenna_doris = Parent("Doris", "Blue-Green")
#print(jenna_doris.last_name)

brooklyn_doris = Child("Doris", "Blue-Green", "15")
print(brooklyn_doris.last_name)
print(brooklyn_doris.num_toys)

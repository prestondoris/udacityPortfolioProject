class Parent():
	def __init__(self, last_name, eye_color):
		print("Parent Constructor Called")
		self.last_name = last_name
		self.eye_color = eye_color

jenna_doris = Parent("Doris", "Blue-Green")
print(jenna_doris.last_name)
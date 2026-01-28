#describing my favorite animal

class animal:
	"""docstring for animal"""
	def __init__(self, arm_length, leg_length, num_eyes, has_tail, is_furry):
		#physical characteristics
		self.arm_length = arm_length	#float
		self.leg_length = leg_length	#float
		self.num_eyes = num_eyes		#int
		self.has_tail = has_tail		#bool
		self.is_furry = is_furry		#bool

	def describe(self):
		print("This is my favorite animal: a cat.")
		print(f"Arm length: {self.arm_length}")
		print(f"Leg length: {self.leg_length}")
		print(f"Number of eyes: {self.num_eyes}")
		print(f"Has a tail: {self.has_tail}")
		print(f"Is furry: {self.is_furry}")

#The deatil number
def main():
	Cat = animal(
		arm_length=0.25,
		leg_length=0.35,
		num_eyes=2,
		has_tail=True,
		is_furry=True
	)

	#describing the animal
	Cat.describe()

main()
import random


class game2:
	data = [
	[[0, 0], [0, 0]],
	[[0, 0], [0, 1]],
	[[0, 0], [1, 0]],
	[[0, 0], [1, 1]],
	[[0, 1], [0, 0]],
	[[0, 1], [0, 1]],
	[[0, 1], [1, 0]],
	[[0, 1], [1, 1]],
	[[1, 0], [0, 0]],
	[[1, 0], [0, 1]],
	[[1, 0], [1, 0]],
	[[1, 0], [1, 1]],
	[[1, 1], [0, 0]],
	[[1, 1], [0, 1]],
	[[1, 1], [1, 0]],
	[[1, 1], [1, 1]],
	]
	
	def play(self, game, bit1, bit2):
		return self.data[game][bit1][bit2]
		
		
class mesh:
	bit = []
	
	def __init__(self):
		for i in range(16):
			self.bit.append(random.randint(0, 1))
			
	def play(self):
		game = self.bit[0] + (2 * self.bit[1]) + (4 * self.bit[2]) + (8 * self.bit[3])
		inaddr1 = (self.bit[4] + (2 * self.bit[5]) + (4 * self.bit[6]) + (8 * self.bit[7]))
		inaddr2 = (self.bit[8] + (2 * self.bit[9]) + (4 * self.bit[10]) + (8 * self.bit[11]))
		outaddr = (self.bit[12] + (2 * self.bit[13]) + (4 * self.bit[14]) + (8 * self.bit[15]))
		in1 = self.bit[inaddr1]
		in2 = self.bit[inaddr2]
		out = game2.play(game, in1, in2)
		self.bit[outaddr] = out
		
	def print(self):
		for i in range(16):
			print(self.bit[i], end="")
			print(" ", end="")
		print()
		
		
m = mesh()
m.print()


# mist


# mob

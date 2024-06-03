import os
import random
import time


def clear():
	command = "clear"
	if os.name in ("nt", "dos"):
		command = "cls"
		os.system(command)


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

g2 = game2();

class mesh:
	bit = []

	def __init__(self):
		for i in range(16):
			self.bit.append(random.randrange(2))

	def mutate(self):
		self.bit[random.randrange(16)] = random.randrange(2)

	def play(self, other):
		game = self.bit[0] + (2 * self.bit[1]) + (4 * self.bit[2]) + (8 * self.bit[3])
		inaddr1 = self.bit[4] + (2 * self.bit[5]) + (4 * self.bit[6]) + (8 * self.bit[7])
		inaddr2 = self.bit[8] + (2 * self.bit[9]) + (4 * self.bit[10]) + (8 * self.bit[11])
		outaddr = self.bit[12] + (2 * self.bit[13]) + (4 * self.bit[14]) + (8 * self.bit[15])
		in1 = other.bit[inaddr1]
		in2 = other.bit[inaddr2]
		out = g2.play(game, in1, in2)
		other.bit[outaddr] = out
		
	def print(self):
		for i in range(16):
			print(self.bit[i], end="")
			print(" ", end="")
		print()


# m = mesh()
# m.print()


class mist:
	size = 8
	meshes = []
	focus = []
	
	def __init__(self):
		for i in range(self.size):
			self.meshes.append(mesh())
			self.focus.append(random.randrange(self.size))
	
	def play(self):
		for i in range(self.size):
			mesh = self.meshes[i]
			other = self.meshes[self.focus[i]]
			mesh.play(other)
			self.focus[i] = random.randrange(self.size)
			if 0 == random.randrange(self.size):
				other.mutate()
		
	def print(self):
		for mesh in self.meshes:
			mesh.print()


m = mist()
for i in range(1000):
	clear()
	m.play()
	m.print()
	time.sleep(1 / 24)


# mob
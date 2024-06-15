import console
import random
import time


def clear():
	console.clear()


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

	def face(self):
		value = 1
		face = 97
		for place in range(4):
			face += self.bits[place] * value
			value *= 2
		return face

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


if False:
	m = mesh()
	m.print()


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


if True:
	m = mist()
	while True:
		m.play()
		clear()
		m.print()
		time.sleep(1 / 8)


class mob:
	dim = 8
	meshes = []
	focus = []

	def finddatamesh(self, i, j):
		x, y = xyfromi(focus[i][j])
		c = wrap(i + x, dim)
		d = wrap(j + y, dim)
		return meshes[c][d]

	def play(self):
		return

	def print(self):
		return

	def xyfromi(self, i):
		if 0 == i:
			return -1, -1
		elif 1 == i:
			return 0, -1
		elif 2 == i:
			return 1, -1
		elif 3 == i:
			return -1, 0
		elif 4 == i:
			return 0, 0
		elif 5 == i:
			return 1, 0
		elif 6 == i:
			return -1, 1
		elif 7 == i:
			return 0, 1
		elif 8 == i:
			return 1, 1

if False:
	m = mob()
	while True:
		m.play()
		clear()
		m.print()
		time.sleep(1 / 8)
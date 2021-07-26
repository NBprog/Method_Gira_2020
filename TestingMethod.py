from math import cos, sin, sqrt, e, pi, pow
from SystemODY import *

class MethodRungeKutta2D():
	def __init__(self):
		self.iteration = 1000
		self.step = 0.1
		self.startX = 0
		self.startY = 0
		self.time = 0
		self.eps = 0.0001
		self.arrayPointRungeX = []
		self.arrayPointRungeY = []
		self.arrayPointGiraX = []
		self.arrayPointGiraY = []
		self.dictionary = {'alfa1' : 0, 'alfa2' : 0, 'alfa3' : 0, 'beta1' : 0, 'beta2' : 0, 'beta3' : 0}
		self.dictTime = {}
		self.cos = cos
		self.sin = sin
		self.sqrt = sqrt
		self.e = e
		self.pi = pi
		self.pow = pow

	def setStep(self,step):
		self.step = step
	def setIter(self, iter):
		self.iteration = iter

	def startMethodRunge(self, function1, function2, startFunctionX, startFunctionY, **kwargs):
		self.dictionary["cos"] = self.cos
		self.dictionary["sin"] = self.sin
		self.dictionary["sqrt"] = self.sqrt
		self.dictionary["e"] = self.e
		self.dictionary["pi"] = self.pi
		self.dictionary["pow"] = self.pow
		for i in range(self.iteration):
			for key, value in kwargs.items():
				if key == "w" or key == "v":
					self.dictionary[key] = value
					continue
				if self.time - value > 0 :
					arrayPoints =  self.dictTime.get(round(self.time - value, 10) )
					if key.find("alfa") != -1:
						self.dictionary[key] = arrayPoints[0]
					if key.find("beta") != -1:
						self.dictionary[key] = arrayPoints[1]
				else:
					t = self.time - value
					self.dictionary["t"] = t
					if key.find("alfa") != -1:
						self.dictionary[key]  = eval(startFunctionX, self.dictionary)
					if key.find("beta") != -1:
						self.dictionary[key]  = eval(startFunctionY, self.dictionary)

			if self.time == 0 :
				t = self.time
				self.startX = eval(startFunctionX)
				self.startY = eval(startFunctionY)

			self.dictionary['x'] = self.startX
			self.dictionary['y'] = self.startY
			self.dictionary['t'] = self.time

			k1x = self.step * eval(function1, self.dictionary)
			k1y = self.step * eval(function2, self.dictionary)

			self.dictionary['x'] = self.startX + k1x/2
			self.dictionary['y'] = self.startY + k1y/2
			self.dictionary['t'] = self.time + self.step/2 

			k2x = self.step * eval(function1, self.dictionary)
			k2y = self.step * eval(function2, self.dictionary)

			self.dictionary['x'] = self.startX + k2x/2
			self.dictionary['y'] = self.startY + k2y/2
			self.dictionary['t'] = self.time + self.step/2 

			k3x = self.step * eval(function1, self.dictionary)
			k3y = self.step * eval(function2, self.dictionary)

			self.dictionary['x'] = self.startX + k3x/2
			self.dictionary['y'] = self.startY + k3y/2
			self.dictionary['t'] = self.time + self.step

			k4x = self.step * eval(function1, self.dictionary)
			k4y = self.step * eval(function2, self.dictionary)

			self.arrayPointRungeX.append(self.startX)
			self.arrayPointRungeY.append(self.startY)
			self.dictTime[round(self.time, 10)] = [self.startX, self.startY]

			#if abs(self.startX) < 100000 and abs(self.startY) < 100000 :
			self.startX += self.result(k1x, k2x, k3x, k4x)
			self.startY += self.result(k1y, k2y, k3y, k4y)
			self.time += self.step

	def get4Point(self, function1, function2, startFunctionX, startFunctionY, **kwargs):
		self.dictionary["cos"] = self.cos
		self.dictionary["sin"] = self.sin
		self.dictionary["sqrt"] = self.sqrt
		self.dictionary["e"] = self.e
		self.dictionary["pi"] = self.pi
		self.dictionary["pow"] = self.pow
		for i in range(4):
			if key == "w" or key == "v":
				self.dictionary[key] = value
				continue
			for key, value in kwargs.items():
				if self.time - value > 0 :
					arrayPoints =  self.dictTime.get(round(self.time - value, 10) )
					if key.find("alfa") != -1:
						self.dictionary[key] = arrayPoints[0]
					if key.find("beta") != -1:
						self.dictionary[key] = arrayPoints[1]
				else:
					t = self.time - value
					self.dictionary["t"] = t
					if key.find("alfa") != -1:
						self.dictionary[key]  = eval(startFunctionX, self.dictionary)
					if key.find("beta") != -1:
						self.dictionary[key]  = eval(startFunctionY, self.dictionary)

			if self.time == 0 :
				t = self.time
				self.startX = eval(startFunctionX)
				self.startY = eval(startFunctionY)

			self.dictionary['x'] = self.startX
			self.dictionary['y'] = self.startY
			self.dictionary['t'] = self.time

			k1x = self.step * eval(function1, self.dictionary)
			k1y = self.step * eval(function2, self.dictionary)

			self.dictionary['x'] = self.startX + k1x/2
			self.dictionary['y'] = self.startY + k1y/2
			self.dictionary['t'] = self.time + self.step/2 

			k2x = self.step * eval(function1, self.dictionary)
			k2y = self.step * eval(function2, self.dictionary)

			self.dictionary['x'] = self.startX + k2x/2
			self.dictionary['y'] = self.startY + k2y/2
			self.dictionary['t'] = self.time + self.step/2 

			k3x = self.step * eval(function1, self.dictionary)
			k3y = self.step * eval(function2, self.dictionary)

			self.dictionary['x'] = self.startX + k3x/2
			self.dictionary['y'] = self.startY + k3y/2
			self.dictionary['t'] = self.time + self.step

			k4x = self.step * eval(function1, self.dictionary)
			k4y = self.step * eval(function2, self.dictionary)

			self.arrayPointGiraX.append(self.startX)
			self.arrayPointGiraY.append(self.startY)

			self.dictTime[round(self.time, 10)] = [self.startX, self.startY]
	
			#if abs(self.startX) < 100000 and abs(self.startY) < 100000 :
			self.startX += self.result(k1x, k2x, k3x, k4x)
			self.startY += self.result(k1y, k2y, k3y, k4y)
			self.time += self.step

	def result (self, k1, k2, k3, k4):
		return 1/6 * (k1 + 2*k2 + 2*k3 + k4)


# def function1(t, x, y):
# 	return 0.1 * (1 - x) * x + 0.9 * (y - x)
# def function2(t, x, y):
# 	return 0.1 * (1 - y) * y + 0.9 * (x - y)


# dict = {1 : [1,2,3], 2 : [3,4,5]}
# print(dict[1])

# k = MethodRungeKuttaMerson2D()
# k.setStep(0.01)
# k.startMethodRunge("y + 0.01*alfa1", "4*(1 - x*x )*y - x + 0.01*beta1", "sin(t)", "cos(t)", alfa1 = 2, beta1 = 2)
# print(k.arrayPointRungeX)
# print(k.arrayPointRungeY)
# print(k.arrayPointRungeZ)

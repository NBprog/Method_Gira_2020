from math import cos, sin, sqrt, e, pi, pow
from SystemODY import *

class MethodRungeKuttaMerson2D():
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
					self.dictionary['t'] = t
					if key.find("alfa") != -1:
						self.dictionary[key]  = eval(startFunctionX, self.dictionary)
					if key.find("beta") != -1:
						self.dictionary[key]  = eval(startFunctionY, self.dictionary)

			if self.time == 0 :
				t = self.time
				self.startX = eval(startFunctionX, self.dictionary)
				self.startY = eval(startFunctionY, self.dictionary)

			self.dictionary['x'] = self.startX
			self.dictionary['y'] = self.startY
			self.dictionary['t'] = self.time

			k1x = 1/3 * self.step * eval(function1, self.dictionary)
			k1y = 1/3 * self.step * eval(function2, self.dictionary)

			self.dictionary['x'] = self.startX + k1x
			self.dictionary['y'] = self.startY + k1y
			self.dictionary['t'] = self.time + 1/3 * self.step 

			k2x = 1/3 * self.step * eval(function1, self.dictionary)
			k2y = 1/3 * self.step * eval(function2, self.dictionary)

			self.dictionary['x'] = self.startX + 1/2 * k1x + 1/2 * k2x
			self.dictionary['y'] = self.startY + 1/2 * k1y + 1/2 * k2y
			self.dictionary['t'] = self.time + 1/3 * self.step 

			k3x = 1/3 * self.step * eval(function1, self.dictionary)
			k3y = 1/3 * self.step * eval(function2, self.dictionary)

			self.dictionary['x'] = self.startX + 3/8*k1x + 9/8*k3x
			self.dictionary['y'] = self.startY + 3/8*k1y + 9/8*k3y
			self.dictionary['t'] = self.time + 1/2 * self.step

			k4x = 1/3 * self.step * eval(function1, self.dictionary)
			k4y = 1/3 * self.step * eval(function2, self.dictionary)

			self.dictionary['x'] = self.startX + 3/2*k1x - 9/2*k3x + 6*k4x
			self.dictionary['y'] = self.startY + 3/2*k1y - 9/2*k3y + 6*k4y
			self.dictionary['t'] = self.time + self.step

			k5x = 1/3 * self.step * eval(function1, self.dictionary)
			k5y = 1/3 * self.step * eval(function2, self.dictionary)

			delta1 = k1x - 9/2*k3x + 4*k4x - 1/2*k5x
			delta2 = k1y - 9/2*k3y + 4*k4y - 1/2*k5y

			
			self.arrayPointRungeX.append(self.startX)
			self.arrayPointRungeY.append(self.startY)
			self.dictTime[round(self.time, 10)] = [self.startX, self.startY]

			#if abs(self.startX) < 100000 and abs(self.startY) < 100000 :
			self.startX += self.result(k1x, k4x, k5x)
			self.startY += self.result(k1y, k4y, k5y)
			self.time += self.step

	def get4Point(self, function1, function2, startFunctionX, startFunctionY, **kwargs):
		self.dictionary["cos"] = self.cos
		self.dictionary["sin"] = self.sin
		self.dictionary["sqrt"] = self.sqrt
		self.dictionary["e"] = self.e
		self.dictionary["pi"] = self.pi
		self.dictionary["pow"] = self.pow
		for i in range(4):
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
					self.dictionary['t'] = t
					if key.find("alfa") != -1:
						self.dictionary[key]  = eval(startFunctionX, self.dictionary)
					if key.find("beta") != -1:
						self.dictionary[key]  = eval(startFunctionY, self.dictionary)

			if self.time == 0 :
				t = self.time
				self.startX = eval(startFunctionX, self.dictionary)
				self.startY = eval(startFunctionY, self.dictionary)

			self.dictionary['x'] = self.startX
			self.dictionary['y'] = self.startY
			self.dictionary['t'] = self.time

			k1x = 1/3 * self.step * eval(function1, self.dictionary)
			k1y = 1/3 * self.step * eval(function2, self.dictionary)

			self.dictionary['x'] = self.startX + k1x
			self.dictionary['y'] = self.startY + k1y
			self.dictionary['t'] = self.time + 1/3 * self.step 

			k2x = 1/3 * self.step * eval(function1, self.dictionary)
			k2y = 1/3 * self.step * eval(function2, self.dictionary)

			self.dictionary['x'] = self.startX + 1/2 * k1x + 1/2 * k2x
			self.dictionary['y'] = self.startY + 1/2 * k1y + 1/2 * k2y
			self.dictionary['t'] = self.time + 1/3 * self.step 

			k3x = 1/3 * self.step * eval(function1, self.dictionary)
			k3y = 1/3 * self.step * eval(function2, self.dictionary)

			self.dictionary['x'] = self.startX + 3/8*k1x + 9/8*k3x
			self.dictionary['y'] = self.startY + 3/8*k1y + 9/8*k3y
			self.dictionary['t'] = self.time + 1/2 * self.step

			k4x = 1/3 * self.step * eval(function1, self.dictionary)
			k4y = 1/3 * self.step * eval(function2, self.dictionary)

			self.dictionary['x'] = self.startX + 3/2*k1x - 9/2*k3x + 6*k4x
			self.dictionary['y'] = self.startY + 3/2*k1y - 9/2*k3y + 6*k4y
			self.dictionary['t'] = self.time + self.step

			k5x = 1/3 * self.step * eval(function1, self.dictionary)
			k5y = 1/3 * self.step * eval(function2, self.dictionary)

			delta1 = k1x - 9/2*k3x + 4*k4x - 1/2*k5x
			delta2 = k1y - 9/2*k3y + 4*k4y - 1/2*k5y

			
			self.arrayPointGiraX.append(self.startX)
			self.arrayPointGiraY.append(self.startY)

			self.dictTime[round(self.time, 10)] = [self.startX, self.startY]
	
			self.startX += self.result(k1x, k4x, k5x)
			self.startY += self.result(k1y, k4y, k5y)
			self.time += self.step

	def result (self, k1, k4, k5):
		return 1/2 * (k1 + 4*k4 + k5)




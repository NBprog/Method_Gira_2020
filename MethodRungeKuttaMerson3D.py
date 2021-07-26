from math import cos, sin, sqrt
from SystemODY import *
class MethodRungeKuttaMerson3D():
	def __init__(self):
		self.iteration = 1000
		self.step = 0.1
		self.startX = 0
		self.startY = 0
		self.startZ = 0
		self.time = 0
		self.eps = 0.0001
		self.arrayPointRungeX = []
		self.arrayPointRungeY = []
		self.arrayPointRungeZ = []
		self.arrayPointGiraX = []
		self.arrayPointGiraY = []
		self.arrayPointGiraZ = []
		self.dictionary = {'alfa1': 0, 'alfa2': 0, 'alfa3': 0, 
											 'beta1': 0, 'beta2': 0, 'beta3': 0, 
											 'gamma1': 0, 'gamma2': 0, 'gamma3': 0}
		self.dictTime = {}
		self.cos = cos
		self.sin = sin
		self.sqrt = sqrt

	def setStep(self,step):
		self.step = step
		
	def setIter(self, iter):
		self.iteration = iter

	def startMethodRunge(self, function1, function2, function3, startFunctionX, startFunctionY, startFunctionZ, **kwargs):
		self.dictionary["cos"] = self.cos
		self.dictionary["sin"] = self.sin
		self.dictionary["sqrt"] = self.sqrt
		for i in range(self.iteration):
			for key, value in kwargs.items():
				if self.time - value > 0 :
					arrayPoints =  self.dictTime.get(round(self.time - value, 10) )
					if key.find("alfa") != -1:
						self.dictionary[key] = arrayPoints[0]
					if key.find("beta") != -1:
						self.dictionary[key] = arrayPoints[1]
					if key.find("gamma") != -1:
						self.dictionary[key] = arrayPoints[2]
				else:
					t = self.time - value
					if key.find("alfa") != -1:
						self.dictionary[key]  = eval(startFunctionX)
					if key.find("beta") != -1:
						self.dictionary[key]  = eval(startFunctionY)
					if key.find("gamma") != -1:
						self.dictionary[key]  = eval(startFunctionZ)

			if self.time == 0 :
				t = self.time
				self.startX = eval(startFunctionX)
				self.startY = eval(startFunctionY)
				self.startZ = eval(startFunctionZ)

			self.dictionary['x'] = self.startX
			self.dictionary['y'] = self.startY
			self.dictionary['z'] = self.startZ
			self.dictionary['t'] = self.time	

			k1x = 1/3 * self.step * eval(function1, self.dictionary)
			k1y = 1/3 * self.step * eval(function2, self.dictionary)
			k1z = 1/3 * self.step * eval(function3, self.dictionary)

			self.dictionary['x'] = self.startX + k1x
			self.dictionary['y'] = self.startY + k1y
			self.dictionary['z'] = self.startZ + k1z
			self.dictionary['t'] = self.time + 1/3 * self.step 

			k2x = 1/3 * self.step * eval(function1, self.dictionary)
			k2y = 1/3 * self.step * eval(function2, self.dictionary)
			k2z = 1/3 * self.step * eval(function3, self.dictionary)

			self.dictionary['x'] = self.startX + 1/2 * k1x + 1/2 * k2x
			self.dictionary['y'] = self.startY + 1/2 * k1y + 1/2 * k2y
			self.dictionary['z'] = self.startZ + 1/2 * k1z + 1/2 * k2z
			self.dictionary['t'] = self.time + 1/3 * self.step 

			k3x = 1/3 * self.step * eval(function1, self.dictionary)
			k3y = 1/3 * self.step * eval(function2, self.dictionary)
			k3z = 1/3 * self.step * eval(function3, self.dictionary)

			self.dictionary['x'] = self.startX + 3/8*k1x + 9/8*k3x
			self.dictionary['y'] = self.startY + 3/8*k1y + 9/8*k3y
			self.dictionary['z'] = self.startZ + 3/8*k1z + 9/8*k3z
			self.dictionary['t'] = self.time + 1/2 * self.step

			k4x = 1/3 * self.step * eval(function1, self.dictionary)
			k4y = 1/3 * self.step * eval(function2, self.dictionary)
			k4z = 1/3 * self.step * eval(function3, self.dictionary)

			self.dictionary['x'] = self.startX + 3/2*k1x - 9/2*k3x + 6*k4x
			self.dictionary['y'] = self.startY + 3/2*k1y - 9/2*k3y + 6*k4y
			self.dictionary['z'] = self.startZ + 3/2*k1z - 9/2*k3z + 6*k4z
			self.dictionary['t'] = self.time + self.step

			k5x = 1/3 * self.step * eval(function1, self.dictionary)
			k5y = 1/3 * self.step * eval(function2, self.dictionary)
			k5z = 1/3 * self.step * eval(function3, self.dictionary)

			delta1 = k1x - 9/2*k3x + 4*k4x - 1/2*k5x
			delta2 = k1y - 9/2*k3y + 4*k4y - 1/2*k5y
			delta3 = k1z - 9/2*k3z + 4*k4z - 1/2*k5z

			self.arrayPointRungeX.append(self.startX)
			self.arrayPointRungeY.append(self.startY)
			self.arrayPointRungeZ.append(self.startZ)
			self.dictTime[round(self.time, 10)] = [self.startX, self.startY, self.startZ]

			if abs(self.startX) < 100000 and abs(self.startY) < 100000 and abs(self.startZ) < 100000 :
				self.startX += self.result(k1x, k4x, k5x)
				self.startY += self.result(k1y, k4y, k5y)
				self.startZ += self.result(k1z, k4z, k5z)
				self.time += self.step

	def get4Point(self, function1, function2, function3, startFunctionX, startFunctionY, startFunctionZ, **kwargs):
		self.dictionary["cos"] = self.cos
		self.dictionary["sin"] = self.sin
		self.dictionary["sqrt"] = self.sqrt
		for i in range(4):
			for key, value in kwargs.items():
				if self.time - value >= 0 :
					arrayPoints =  self.dictTime.get(round(self.time - value, 10) )
					if key.find("alfa") != -1:
						self.dictionary[key] = arrayPoints[0]
					if key.find("beta") != -1:
						self.dictionary[key] = arrayPoints[1]
					if key.find("gamma") != -1:
						self.dictionary[key] = arrayPoints[2]
				else:
					t = self.time - value
					if key.find("alfa") != -1:
						self.dictionary[key]  = eval(startFunctionX)
					if key.find("beta") != -1:
						self.dictionary[key]  = eval(startFunctionY)
					if key.find("gamma") != -1:
						self.dictionary[key]  = eval(startFunctionZ)

			if self.time == 0 :
				t = self.time
				self.startX = eval(startFunctionX)
				self.startY = eval(startFunctionY)
				self.startZ = eval(startFunctionZ)

			self.dictionary['x'] = self.startX
			self.dictionary['y'] = self.startY
			self.dictionary['z'] = self.startZ
			self.dictionary['t'] = self.time

			k1x = 1/3 * self.step * eval(function1, self.dictionary)
			k1y = 1/3 * self.step * eval(function2, self.dictionary)
			k1z = 1/3 * self.step * eval(function3, self.dictionary)

			self.dictionary['x'] = self.startX + k1x
			self.dictionary['y'] = self.startY + k1y
			self.dictionary['z'] = self.startZ + k1z
			self.dictionary['t'] = self.time + 1/3 * self.step 

			k2x = 1/3 * self.step * eval(function1, self.dictionary)
			k2y = 1/3 * self.step * eval(function2, self.dictionary)
			k2z = 1/3 * self.step * eval(function3, self.dictionary)

			self.dictionary['x'] = self.startX + 1/2 * k1x + 1/2 * k2x
			self.dictionary['y'] = self.startY + 1/2 * k1y + 1/2 * k2y
			self.dictionary['z'] = self.startZ + 1/2 * k1z + 1/2 * k2z
			self.dictionary['t'] = self.time + 1/3 * self.step 

			k3x = 1/3 * self.step * eval(function1, self.dictionary)
			k3y = 1/3 * self.step * eval(function2, self.dictionary)
			k3z = 1/3 * self.step * eval(function3, self.dictionary)

			self.dictionary['x'] = self.startX + 3/8*k1x + 9/8*k3x
			self.dictionary['y'] = self.startY + 3/8*k1y + 9/8*k3y
			self.dictionary['z'] = self.startZ + 3/8*k1z + 9/8*k3z
			self.dictionary['t'] = self.time + 1/2 * self.step

			k4x = 1/3 * self.step * eval(function1, self.dictionary)
			k4y = 1/3 * self.step * eval(function2, self.dictionary)
			k4z = 1/3 * self.step * eval(function3, self.dictionary)

			self.dictionary['x'] = self.startX + 3/2*k1x - 9/2*k3x + 6*k4x
			self.dictionary['y'] = self.startY + 3/2*k1y - 9/2*k3y + 6*k4y
			self.dictionary['z'] = self.startZ + 3/2*k1z - 9/2*k3z + 6*k4z
			self.dictionary['t'] = self.time + self.step

			k5x = 1/3 * self.step * eval(function1, self.dictionary)
			k5y = 1/3 * self.step * eval(function2, self.dictionary)
			k5z = 1/3 * self.step * eval(function3, self.dictionary)

			delta1 = k1x - 9/2*k3x + 4*k4x - 1/2*k5x
			delta2 = k1y - 9/2*k3y + 4*k4y - 1/2*k5y
			delta3 = k1z - 9/2*k3z + 4*k4z - 1/2*k5z

			self.arrayPointGiraX.append(self.startX)
			self.arrayPointGiraY.append(self.startY)
			self.arrayPointGiraZ.append(self.startZ)

			self.dictTime[round(self.time, 10)] = [self.startX, self.startY, self.startZ]
	
			if abs(self.startX) < 100000 and abs(self.startY) < 100000 and abs(self.startZ) < 100000 :
				self.startX += self.result(k1x, k4x, k5x)
				self.startY += self.result(k1y, k4y, k5y)
				self.startZ += self.result(k1z, k4z, k5z)
				self.time += self.step
				self.dictionary['t'] = self.time

	def result (self, k1, k4, k5):
		return 1/2 * (k1 + 4*k4 + k5)


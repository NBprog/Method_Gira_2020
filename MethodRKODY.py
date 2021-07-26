from math import cos, sin, sqrt, e, pi, pow

class MethodRKODY():
	def __init__(self, step = 0.1, iteration = 1000, startX = 0.4, time = 0):
		if type(step) == str or type(iteration) == str or type(startX) == str or type(time) == str :
			raise Exception("Invalid Type")
		self.step = step
		self.iteration = iteration
		self.startX = startX
		self.time = time
		self.arrayPointGiraX = []
		self.arrayPointGiraT = []
		self.arrayPointRungeX = []
		self.arrayPointRungeT = []
		self.dictionary = {'alfa1' : 0, 'alfa2' : 0, 'alfa3' : 0}
		self.dictTime = {}
		self.cos = cos
		self.sin = sin
		self.sqrt = sqrt
		self.e = e
		self.pi = pi
		self.pow = pow

	def setStep(self,step):
		self.step = step
	def setIter(self, iteration):
		self.iteration = iteration
	def setStartPoint(self, x):
		self.startX = x

	def startMethodRunge(self, function1, startfunctionX, **kwargs):
		self.dictionary["cos"] = self.cos
		self.dictionary["sin"] = self.sin
		self.dictionary["sqrt"] = self.sqrt
		self.dictionary["e"] = self.e
		self.dictionary["pi"] = self.pi
		self.dictionary["pow"] = self.pow
		for i in range(self.iteration):
			for key, value in kwargs.items():
				if key == "w":
					self.dictionary[key] = value
					continue
				if self.time - value > 0 :
					arrayPoints =  self.dictTime.get(round(self.time - value, 10) )
					if key.find("alfa") != -1:
						self.dictionary[key] = arrayPoints[0]
				else:
					t = self.time - value
					if key.find("alfa") != -1:
						self.dictionary[key]  = eval(startfunctionX)

			if i == 0 :
				t = self.time
				self.startX = eval(startfunctionX)

			self.dictionary['x'] = self.startX
			self.dictionary['t'] = self.time
		
			k1x = eval(function1, self.dictionary)

			self.dictionary['x'] = self.startX + k1x * self.step / 2
			self.dictionary['t'] = self.time + self.step / 2

			k2x = eval(function1, self.dictionary)

			self.dictionary['x'] = self.startX + k2x * self.step / 2
			self.dictionary['t'] = self.time + self.step / 2

			k3x = eval(function1, self.dictionary)

			self.dictionary['x'] = self.startX + k3x * self.step
			self.dictionary['t'] = self.time + self.step

			k4x = eval(function1, self.dictionary)

			self.arrayPointRungeX.append(self.startX)
			self.arrayPointRungeT.append(self.time)
			self.dictTime[round(self.time, 10)] = [self.startX]

			if abs(self.startX) < 100000 and abs(self.time) < 100000 :
				self.startX += self.result(k1x, k2x, k3x, k4x)
				self.time += self.step

	def get4Point(self, function1, startfunctionX, **kwargs):
		self.dictionary["cos"] = self.cos
		self.dictionary["sin"] = self.sin
		self.dictionary["sqrt"] = self.sqrt
		self.dictionary["e"] = self.e
		self.dictionary["pi"] = self.pi
		self.dictionary["pow"] = self.pow
		for i in range(4):
			for key, value in kwargs.items():
				if key == "w":
					self.dictionary[key] = value
					continue
				if self.time - value > 0 :
					arrayPoints =  self.dictTime.get(round(self.time - value, 10) )
					if key.find("alfa") != -1:
						self.dictionary[key] = arrayPoints[0]
				else:
					t = self.time - value
					if key.find("alfa") != -1:
						self.dictionary[key]  = eval(startfunctionX)

			if i == 0 :
				t = self.time
				self.startX = eval(startfunctionX)

			self.dictionary['x'] = self.startX
			self.dictionary['t'] = self.time
		
			k1x = eval(function1, self.dictionary)

			self.dictionary['x'] = self.startX + k1x * self.step / 2
			self.dictionary['t'] = self.time + self.step / 2

			k2x = eval(function1, self.dictionary)

			self.dictionary['x'] = self.startX + k2x * self.step / 2
			self.dictionary['t'] = self.time + self.step / 2

			k3x = eval(function1, self.dictionary)

			self.dictionary['x'] = self.startX + k3x * self.step
			self.dictionary['t'] = self.time + self.step

			k4x = eval(function1, self.dictionary)

			self.arrayPointGiraX.append(self.startX)
			self.arrayPointGiraT.append(self.time)
			self.dictTime[round(self.time, 10)] = [self.startX]

			if abs(self.startX) < 100000 and abs(self.time) < 100000 :
				self.startX += self.result(k1x, k2x, k3x, k4x)
				self.time += self.step		

	def result (self,k1,k2,k3,k4):
		return self.step / 6 * (k1 + 2*k2 + 2*k3 + k4)

# k = MethodRKODY()
# k.setStep(0.1)
# k.startMethodRunge("0.3*x + 0.2*alfa1", "1", alfa1 = 1, alfa2 = 1, alfa3 = 1)
#print(k.arrayPointRungeT)
#print(k.arrayPointRungeX)
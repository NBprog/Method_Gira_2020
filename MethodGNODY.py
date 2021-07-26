from math import *
from MethodRKODY import *
from sympy import *

class MethodGNODY():
	def __init__(self, iteration = 1000, step = 0.1):
		if type(step) == str or type(iteration) == str :
			raise Exception("Invalid Type")

		self.iteration = iteration
		self.step = step
		self.a0 = 25/12
		self.a1 = -4
		self.a2 = 3
		self.a3 = -4/3
		self.a4 = 1/4
		self.methodRunge = MethodRKODY()
		self.startVectorX = 0
		self.pointsMethodGiraX = []
		self.pointsMethodGiraT = []
		self.resultX = 0
		self.resultT = 0
		self.PointGX = []
		self.PointGT = []
		self.eps = 0.001
		self.counter = 0
		self.time = 0

		#Для вычисленных значений
		self.dictionaryTime = {}

		# Для окружения
		self.dictionary = {}

	def setStep(self, step):
		self.methodRunge.setStep(step)
		self.step = step 

	def setIter(self, iteration):
		self.iteration = iteration

	def getArrayPoints(self, function1, startfunctionX, **kwargs):
		self.methodRunge.get4Point(function1, startfunctionX, **kwargs)
		self.dictionary = self.methodRunge.dictionary
		self.dictionaryTime = self.methodRunge.dictTime
		self.time = self.step*4
		self.pointsMethodGiraX = self.methodRunge.arrayPointGiraX
		self.pointsMethodGiraT = self.methodRunge.arrayPointGiraT
		self.startVectorX = self.pointsMethodGiraX[3]
		self.startVectorT = self.pointsMethodGiraT[3]

	def shift(self):
		for i in range(3):
			self.pointsMethodGiraX[i] = self.pointsMethodGiraX[i+1]

	def vectorHelper(self, function1, startfunctionX, **kwargs):
		self.dictionary['x'] = self.startVectorX
		a = self.step / self.a0 * eval(function1, self.dictionary)
		b = self.a1 / self.a0 * self.pointsMethodGiraX[3]
		c = self.a2 / self.a0 * self.pointsMethodGiraX[2]
		d = self.a3 / self.a0 * self.pointsMethodGiraX[1]
		e = self.a4 / self.a0 * self.pointsMethodGiraX[0]
		resultVectorX = self.startVectorX - a + b + c + d + e
		return resultVectorX

	def resultArray(self, function1, startfunctionX, **kwargs):
		vecX = self.vectorHelper(function1, startfunctionX, **kwargs)

		self.dictionary['x'] = self.startVectorX

		X1G = 1 -self.step / self.a0 * float(eval(str(self.dx1), self.dictionary))

		new_x = self.startVectorX - vecX / X1G

		if abs(new_x - self.startVectorX) >= self.eps  and  self.counter < 100 :
			self.startVectorX = new_x
			self.counter += 1
			return self.resultArray(function1, startfunctionX, **kwargs)
		else:
			self.shift()
			self.startVectorX = new_x
			if self.counter < 100 :
				self.resultX = new_x
			self.counter = 0
			self.pointsMethodGiraX[3] = new_x
			return self.resultX

	def startComputing(self, function1, startfunctionX, **kwargs):
		self.getArrayPoints(function1, startfunctionX, **kwargs)
		resX=0
		x = symbols('x')
		self.dx1 = diff(function1, x)

		for i in range(4):
			self.PointGX.append( self.pointsMethodGiraX[i])
			self.PointGT.append( self.pointsMethodGiraT[i])

		for i in range(self.iteration - 4):
			for key, value in kwargs.items():
				if self.time - value > 0 :
					arrayPoints =  self.dictionaryTime.get(round(self.time - value, 10) )

					if key.find("alfa") != -1:
						self.dictionary[key] = arrayPoints[0]

				else:
					t = self.time - value
					if key.find("alfa") != -1:
						self.dictionary[key]  = eval(startfunctionX)

			if abs(resX) < 100000:
				resX  = self.resultArray(function1, startfunctionX, **kwargs)

			self.PointGX.append(resX)
			self.PointGT.append(self.time)
			self.dictionaryTime[round(self.time, 10)] = [resX]
			self.time = self.time + self.step 
			self.dictionary['t'] = self.time

		return self.PointGX, self.PointGT


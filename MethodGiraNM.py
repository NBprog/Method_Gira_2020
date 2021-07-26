from MethodRungeKutta import *
from math import *
from SystemODY import *

class MethodGiraNM():
	def __init__(self, iteration = 1000, step = 0.01):
		if type(step) == str or type(iteration) == str :
			raise Exception("Invalid Type")
			
		self.iteration = iteration
		self.step = step
		self.a0 = 25/12
		self.a1 = -4
		self.a2 = 3
		self.a3 = -4/3
		self.a4 = 1/4
		self.methodRunge = MethodRungeKutta4()
		self.startVectorX = 0
		self.startVectorY = 0 
		self.pointsMethodGiraX = []
		self.pointsMethodGiraY = []
		self.resultX = 0
		self.resultY = 0
		self.PointGX = []
		self.PointGY = []
		self.constX = 0
		self.constY = 0
		self.eps = 0.0001
		self.counter = 0

	def setStartPoint(self, x, y):
		self.methodRunge.setStartPoint(x, y)

	def setStep(self, step):
		self.methodRunge.setStep(step)
		self.step = step

	def setIter(self, iteration):
		self.iteration = iteration

	def getArrayPoints(self, systemODY):
		self.methodRunge.startMethodRunge(systemODY)
		self.pointsMethodGiraX = self.methodRunge.arrayPointGiraX
		self.pointsMethodGiraY = self.methodRunge.arrayPointGiraY
		self.startVectorX = self.pointsMethodGiraX[3]
		self.startVectorY = self.pointsMethodGiraY[3] 

	def shift(self):
		for i in range(3):
			self.pointsMethodGiraX[i] = self.pointsMethodGiraX[i+1]
			self.pointsMethodGiraY[i] = self.pointsMethodGiraY[i+1]

	def vectorHelper(self, systemODY):
		resultVectorX = []
		resultVectorY = []
		a = self.step / self.a0 * systemODY.function1(self.startVectorX, self.startVectorY)
		b = self.a1 / self.a0 * self.pointsMethodGiraX[3]
		c = self.a2 / self.a0 * self.pointsMethodGiraX[2]
		d = self.a3 / self.a0 * self.pointsMethodGiraX[1]
		e = self.a4 / self.a0 * self.pointsMethodGiraX[0]
		resultVectorX = self.startVectorX - a + b + c + d + e
		a = self.step / self.a0 * systemODY.function2(self.startVectorX, self.startVectorY)
		b = self.a1 / self.a0 * self.pointsMethodGiraY[3]
		c = self.a2 / self.a0 * self.pointsMethodGiraY[2]
		d = self.a3 / self.a0 * self.pointsMethodGiraY[1]
		e = self.a4 / self.a0 * self.pointsMethodGiraY[0]
		resultVectorY = self.startVectorY - a + b + c + d + e
		return resultVectorX, resultVectorY

	def resultArray(self, system):
		vecX, vecY = self.vectorHelper(system)

		new_x = self.startVectorX - (system.X1ReverseG(self.startVectorX,self.startVectorY)*vecX 
															+ system.Y1ReverseG(self.startVectorX,self.startVectorY)*vecY)
		new_y = self.startVectorY - (system.X2ReverseG(self.startVectorX,self.startVectorY)*vecX 
															+ system.Y2ReverseG(self.startVectorX,self.startVectorY)*vecY)

		if sqrt((new_x - self.startVectorX)**2 + (new_y - self.startVectorY)**2 ) >= self.eps and self.counter < 100 :
			self.startVectorX = new_x
			self.startVectorY = new_y
			self.counter += 1
			return self.resultArray(system)

		else:

			self.shift()
			self.startVectorX = new_x
			self.startVectorY = new_y

			if self.counter < 100 :
				self.resultX = new_x
				self.resultY = new_y

			self.counter = 0
			self.pointsMethodGiraX[3] = new_x
			self.pointsMethodGiraY[3] = new_y
			return self.resultX, self.resultY

	def startComputing(self, system):

		self.getArrayPoints(system)

		resX=0
		resY=0

		for i in range(4):
			self.PointGX.append( self.pointsMethodGiraX[i])
			self.PointGY.append( self.pointsMethodGiraY[i])

		for i in range(self.iteration - 4):
			if(abs(resX) < 100000 and abs(resY) < 100000) :
				resX,resY = self.resultArray(system)

			self.PointGX.append(resX)
			self.PointGY.append(resY)

		return self.PointGX, self.PointGY


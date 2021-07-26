from MethodRungeKutta import *
from SystemODY import *
from math import *


class MethodGira :
	def __init__(self, step = 0.01, iteration = 1000, startX = 0.4, startY = 0.75):
		if type(step) == str or type(iteration) == str or type(startX) == str or type(startY) == str :
			raise Exception("Invalid Type")
		self.step = step
		self.iteration = iteration
		self.startX = startX
		self.startY = startY
		self.methodRunge = MethodRungeKutta4() 
		self.arrayStartPointX = []
		self.arrayStartPointY = []
		self.arrayPointSIMX = []
		self.arrayPointSIMY = []
		self.constX = 0
		self.constY = 0
		self.eps = 0.0001
		self.startVectorX = 0
		self.startVectorY = 0
		self.a0 = 25/12
		self.a1 = -4
		self.a2 = 3
		self.a3 = -4/3
		self.a4 = 1/4
		self.counter = 0

	def setStartPoint(self, x, y) :
		self.methodRunge.setStartPoint(x, y)
	def setStep(self, step) :
		self.methodRunge.setStep(step)
		self.step = step
	def setIter(self, iteration):
		self.iteration = iteration 

	def getArrayRunge(self, system):
		self.methodRunge.startMethodRunge(system)
		self.arrayStartPointX = self.methodRunge.arrayPointGiraX
		self.arrayStartPointY = self.methodRunge.arrayPointGiraY
		self.startVectorX = self.arrayStartPointX[3]
		self.startVectorY = self.arrayStartPointY[3]

	def calculationConst(self):
		a = (-1) * self.arrayStartPointX[0] * self.a4/self.a0   
		b = (-1) * self.arrayStartPointX[1] * self.a3/self.a0
		c = (-1) * self.arrayStartPointX[2] * self.a2/self.a0
		d = (-1) * self.arrayStartPointX[3] * self.a1/self.a0
		self.constX = a + b + c + d
		a = (-1) * self.arrayStartPointY[0] * self.a4/self.a0   
		b = (-1) * self.arrayStartPointY[1] * self.a3/self.a0
		c = (-1) * self.arrayStartPointY[2] * self.a2/self.a0
		d = (-1) * self.arrayStartPointY[3] * self.a1/self.a0
		self.constY = a + b + c + d

	def shift(self):
		for i in range(3) :
			self.arrayStartPointX[i] = self.arrayStartPointX[i+1]
			self.arrayStartPointY[i] = self.arrayStartPointY[i+1]

	def startCalculate(self, system):
		self.calculationConst()
		x_new = 0
		y_new = 0
		x_new = 12/25 * self.step * system.function1(self.startVectorX, self.startVectorY) + self.constX
		y_new = 12/25 * self.step * system.function2(self.startVectorX, self.startVectorY) + self.constY
		if sqrt((x_new - self.startVectorX)**2 + (y_new - self.startVectorY)**2) >= self.eps and self.counter < 100 :
			self.startVectorX = x_new 
			self.startVectorY = y_new 
			self.counter += 1
			return self.startCalculate(system)
		else:
			self.shift()
			self.startVectorX = x_new
			self.startVectorY = y_new
			if (self.counter < 100):
				self.arrayStartPointX[3] = x_new
				self.arrayStartPointY[3] = y_new
			self.counter = 0
			return self.arrayStartPointX, self.arrayStartPointY

	def Iteration(self, system):
		self.getArrayRunge(system)
		for i in range(4) :
			self.arrayPointSIMX.append(self.arrayStartPointX[i])
			self.arrayPointSIMY.append(self.arrayStartPointY[i])
		for i in range(self.iteration - 4):
			if(abs(self.arrayStartPointX[3]) < 10000 and abs(self.arrayStartPointY[3])<100000):
				self.startCalculate(system)
			self.arrayPointSIMX.append(self.arrayStartPointX[3])
			self.arrayPointSIMY.append(self.arrayStartPointY[3])

# всё что ниже надо убрать
def function1(x, y) : 
	return 0.1 * (1 - x) * x + 0.9 * (y - x)
def function2(x, y) :
	return 0.1 * (1 - y) * y + 0.9 * (x - y)


# system = SystemODY()
# k = MethodGira()
# k.Iteration(system)
# print(k.arrayPointSIMX)
# print(k.arrayPointSIMY)







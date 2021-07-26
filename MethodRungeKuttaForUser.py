from MethodRungeKutta import *
from math import *
from SystemODY import *

class MethodRungeKutta4ForUser():
	def __init__(self):
		self.iteration = 1000
		self.step = 0.1
		self.startX = 0.4
		self.startY = 0.75
		self.arrayPointRungeX = []
		self.arrayPointRungeY = []
		self.arrayPointGiraX = []
		self.arrayPointGiraY = []

	def setStep(self, step):
		self.step = step
	def setIter(self, iter):
		self.iteration = iter
	def setStartPoint(self, x, y):
		self.startX = x
		self.startY = y

	def startMethodRunge(self, function1, function2, w, v ):
		for i in range(self.iteration):
			x = self.startX
			y = self.startY
			k1x = eval(function1)
			k1y = eval(function2)
			x = self.startX + k1x * self.step / 2
			y = self.startY + k1y * self.step / 2
			k2x = eval(function1)
			k2y = eval(function2)
			x = self.startX + k2x * self.step / 2
			y = self.startY + k2y * self.step / 2
			k3x = eval(function1)
			k3y = eval(function2)
			x = self.startX + k3x * self.step
			y = self.startY + k3y * self.step
			k4x = eval(function1)
			k4y = eval(function2)
			self.arrayPointRungeX.append(self.startX)
			self.arrayPointRungeY.append(self.startY)
			if abs(self.startX)<100000 and abs(self.startY)<100000 :
				self.startX += self.result(k1x, k2x, k3x, k4x)
				self.startY += self.result(k1y, k2y, k3y, k4y)

	def get4Point(self,function1, function2, w, v):
		for i in range(4):
			x = self.startX
			y = self.startY
			k1x = eval(function1)
			k1y = eval(function2)
			x = self.startX + k1x * self.step / 2
			y = self.startY + k1y * self.step / 2
			k2x = eval(function1)
			k2y = eval(function2)
			x = self.startX + k2x * self.step / 2
			y = self.startY + k2y * self.step / 2
			k3x = eval(function1)
			k3y = eval(function2)
			x = self.startX + k3x * self.step
			y = self.startY + k3y * self.step
			k4x = eval(function1)
			k4y = eval(function2)
			self.arrayPointGiraX.append(self.startX)
			self.arrayPointGiraY.append(self.startY)
			if abs(self.startX)<100000 and abs(self.startY)<100000 :
				self.startX += self.result(k1x, k2x, k3x, k4x)
				self.startY += self.result(k1y, k2y, k3y, k4y)

	def result(self, k1, k2, k3, k4):
		return self.step / 6 * (k1 + 2*k2 + 2*k3 + k4)

# k = SystemODY()
# m = MethodRungeKutta4ForUser()
# m.get4Point(k.GetFunction1(), k.GetFunction2(), 0, 0)
# print(m.arrayPointGiraX)
# print(m.arrayPointGiraY)

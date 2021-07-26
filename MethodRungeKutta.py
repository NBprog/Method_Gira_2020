from math import *

class MethodRungeKutta4():
	def __init__(self, step = 0.01, iteration = 1000, startX = 0.4, startY = 0.75):
		if type(step) == str or type(iteration) == str or type(startX) == str or type(startY) == str :
			raise Exception("Invalid Type")
		self.step = step
		self.iteration = iteration
		self.startX = startX
		self.startY = startY
		self.arrayPointGiraX = []
		self.arrayPointGiraY = []
		self.arrayPointRungeX = []
		self.arrayPointRungeY = []

	def setStep(self,step):
		self.step = step
	def setIter(self, iter):
		self.iteration = iter
	def setStartPoint(self, x, y):
		self.startX = x
		self.startY = y

	def startMethodRunge(self, system):
		for i in range(self.iteration):

			k1x = system.function1(self.startX, self.startY)
			k1y = system.function2(self.startX, self.startY)

			k2x = system.function1(self.startX + k1x * self.step / 2, self.startY + k1y * self.step/2)
			k2y = system.function2(self.startX + k1x * self.step / 2, self.startY + k1y * self.step/2)

			k3x = system.function1(self.startX + k2x * self.step/2, self.startY + k2y * self.step/2)
			k3y = system.function2(self.startX + k2x * self.step/2, self.startY + k2y * self.step/2)

			k4x = system.function1(self.startX + k3x * self.step, self.startY + k3y * self.step)
			k4y = system.function2(self.startX + k3x * self.step, self.startY + k3y * self.step)

			if i < 4 :
				self.arrayPointGiraX.append(self.startX)
				self.arrayPointGiraY.append(self.startY)
				self.arrayPointRungeX.append(self.startX)
				self.arrayPointRungeY.append(self.startY)
			else:
				self.arrayPointRungeX.append(self.startX)
				self.arrayPointRungeY.append(self.startY)

			if abs(self.startX) < 100000 and abs(self.startY) < 100000 :
				self.startX += self.result(k1x, k2x, k3x, k4x)
				self.startY += self.result(k1y, k2y, k3y, k4y)

	def result (self, k1, k2, k3, k4):
		return self.step / 6 * (k1 + 2*k2 + 2*k3 + k4)

# не значимые функции(удалить после создания)

# def function1(x, y) : 
# 	return 0.1 * (1 - x) * x + 0.9 * (y - x)
# def function2(x, y) :
# 	return 0.1 * (1 - y) * y + 0.9 * (x - y)
# s = SystemODY()
# k = MethodRungeKutta4()
# k.startMethodRunge(s)
# print(k.arrayPointRungeX)
# print(k.arrayPointRungeY)


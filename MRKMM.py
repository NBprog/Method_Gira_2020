from math import cos, sin, sqrt
from SystemODY import *
class MRKMM():
	def __init__(self):
		self.iteration = 1000
		self.step = 0.2
		self.startX = 2
		self.startY = 0
		self.time = 0
		self.eps = 0.0001
		self.dictionary = {}
		self.arrayPointRungeX = []
		self.arrayPointRungeY = []
		self.arrayPointGiraX = []
		self.arrayPointGiraY = []

	def setStartPoint(self, x, y):
		self.startX = x
		self.startY = y 
	def setStep(self,step):
		self.step = step
	def setIter(self, iteration):
		self.iteration = iteration
	def get4Point(self, function1, function2, w, v):
		i = 0
		while i < 4:
			i+=1
			x = self.startX
			y = self.startY
			t = self.time

			k1x = 1/3 * self.step * eval(function1)
			k1y = 1/3 * self.step * eval(function2)

			x = self.startX + k1x
			y = self.startY + k1y
			t = self.time + 1/3 * self.step 

			k2x = 1/3 * self.step * eval(function1)
			k2y = 1/3 * self.step * eval(function2)

			x = self.startX + 1/2 * k1x + 1/2 * k2x
			y = self.startY + 1/2 * k1y + 1/2 * k2y
			t = self.time + 1/3 * self.step 

			k3x = 1/3 * self.step * eval(function1)
			k3y = 1/3 * self.step * eval(function2)

			x = self.startX + 3/8*k1x + 9/8*k3x
			y = self.startY + 3/8*k1y + 9/8*k3y
			t = self.time + 1/2 * self.step

			k4x = 1/3 * self.step * eval(function1)
			k4y = 1/3 * self.step * eval(function2)

			x = self.startX + 3/2*k1x - 9/2*k3x + 6*k4x
			y = self.startY + 3/2*k1y - 9/2*k3y + 6*k4y
			t = self.time + self.step

			k5x = 1/3 * self.step * eval(function1)
			k5y = 1/3 * self.step * eval(function2)

			delta1 = k1x - 9/2*k3x + 4*k4x - 1/2*k5x
			delta2 = k1y - 9/2*k3y + 4*k4y - 1/2*k5y

			# Автоматический выбор шага
			if delta1 > 5 * self.eps or delta2 > 5 * self.eps :
				self.step = self.step / 2
				i = i - 1 
				continue
			if delta1 < 5/32 * self.eps and delta2 < 5/32 * self.eps:
				self.step = 2*self.step
			self.arrayPointGiraX.append(self.startX)
			self.arrayPointGiraY.append(self.startY)
	
			#if abs(self.startX) < 100000 and abs(self.startY) < 100000 :
			self.startX += self.result(k1x, k4x, k5x)
			self.startY += self.result(k1y, k4y, k5y)
			self.time += self.step

	def result (self, k1, k4, k5):
		return 1/2 * (k1 + 4*k4 + k5)


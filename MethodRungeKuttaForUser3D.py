from MethodRungeKutta import *
from math import *
from SystemODY import *

class MethodRungeKutta4ForUser3D():
	def __init__(self):
		self.iteration = 1000
		self.step = 0.0001
		self.startX = 0.2
		self.startY = 0.2
		self.startZ = 0.2
		self.arrayPointRungeX = []
		self.arrayPointRungeY = []
		self.arrayPointRungeZ = []
		self.arrayPointGiraX = []
		self.arrayPointGiraY = []
		self.arrayPointGiraZ = []

	def setStep(self,step):
		self.step = step
	def setIter(self, iteration):
		self.iteration = iteration
	def setStartPoint(self, x, y, z):
		self.startX = x
		self.startY = y
		self.startZ = z

	def startMethodRunge(self,function1, function2, function3, w, v, alfa, beta):
		for i in range(self.iteration):
			x = self.startX
			y = self.startY
			z = self.startZ
			k1x = eval(function1)
			k1y = eval(function2)
			k1z = eval(function3)
			x = self.startX + k1x * self.step / 2
			y = self.startY + k1y * self.step / 2
			z = self.startZ + k1z * self.step / 2
			k2x = eval(function1) 
			k2y = eval(function2)
			k2z = eval(function3)
			x = self.startX + k2x * self.step / 2
			y = self.startY + k2y * self.step / 2
			z = self.startZ + k2z * self.step / 2
			k3x = eval(function1)
			k3y = eval(function2)
			k3z = eval(function3)
			x = self.startX + k3x * self.step
			y = self.startY + k3y * self.step
			z = self.startZ + k3z * self.step
			k4x = eval(function1)
			k4y = eval(function2)
			k4z = eval(function3)

			self.arrayPointRungeX.append(self.startX)
			self.arrayPointRungeY.append(self.startY)
			self.arrayPointRungeZ.append(self.startZ)
			#if abs(self.startX)<100000 and abs(self.startY)<100000 and abs(self.startZ) < 100000 :
			self.startX += self.result(k1x, k2x, k3x, k4x)
			self.startY += self.result(k1y, k2y, k3y, k4y)
			self.startZ += self.result(k1z, k2z, k3z, k4z)

	def get4Point(self,function1, function2, function3, w, v, alfa, beta):
		for i in range(4):
			x = self.startX
			y = self.startY
			z = self.startZ
			k1x = eval(function1)
			k1y = eval(function2)
			k1z = eval(function3)
			x = self.startX + k1x * self.step / 2
			y = self.startY + k1y * self.step / 2
			z = self.startZ + k1z * self.step / 2
			k2x = eval(function1) 
			k2y = eval(function2)
			k2z = eval(function3)
			x = self.startX + k2x * self.step / 2
			y = self.startY + k2y * self.step / 2
			z = self.startZ + k2z * self.step / 2
			k3x = eval(function1)
			k3y = eval(function2)
			k3z = eval(function3)
			x = self.startX + k3x * self.step
			y = self.startY + k3y * self.step
			z = self.startZ + k3z * self.step
			k4x = eval(function1)
			k4y = eval(function2)
			k4z = eval(function3)
			self.arrayPointGiraX.append(self.startX)
			self.arrayPointGiraY.append(self.startY)
			self.arrayPointGiraZ.append(self.startZ)
			#if abs(self.startX)<100000 and abs(self.startY)<100000 and abs(self.startZ) < 100000 :
			self.startX += self.result(k1x, k2x, k3x, k4x)
			self.startY += self.result(k1y, k2y, k3y, k4y)
			self.startZ += self.result(k1z, k2z, k3z, k4z)

	def result(self, k1, k2, k3, k4):
		return self.step / 6 * (k1 + 2*k2 + 2*k3 + k4)

# m = MethodRungeKutta4ForUser3D()
# m.setStep(0.1)
# m.get4Point("y+3.9*z", "0.9*x*x-y", " 1-x ",  0, 0 , 0, 0)
# print(m.arrayPointGiraX)
# print(m.arrayPointGiraY)
# print(m.arrayPointGiraZ)
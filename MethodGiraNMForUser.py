from MethodRungeKutta import *
from MethodRungeKuttaForUser import * 
from MRKMM import *
from math import *
from SystemODY import *
from sympy import *

class MethodGiraNMForUser():
	def __init__(self, iteration = 1000, step = 0.1):
		if type(step) == str or type(iteration) == str :
			raise Exception("Invalid Type")
		self.iteration = iteration
		self.step = step
		self.counter = 0
		self.a0 = 25/12
		self.a1 = -4
		self.a2 = 3
		self.a3 = -4/3
		self.a4 = 1/4
		self.methodRunge = MRKMM()
		self.startVectorX = 0
		self.startVectorY = 0 
		self.pointsMethodGiraX = []
		self.pointsMethodGiraY = []
		self.resultX = 0
		self.resultY = 0
		self.PointGX = []
		self.PointGY = []
		self.eps = 0.001
		self.counter = 0

	def setStartPoint(self, x, y):
		self.methodRunge.setStartPoint(x, y)
	def setStep(self, step):
		self.methodRunge.setStep(0.000001)
		self.step = step 
	def setIter(self, iteration):
		self.iteration = iteration

	def getArrayPoints(self, function1, function2, w , v):
		self.methodRunge.get4Point(function1, function2, w ,v)
		self.pointsMethodGiraX = self.methodRunge.arrayPointGiraX
		self.pointsMethodGiraY = self.methodRunge.arrayPointGiraY
		self.startVectorX = self.pointsMethodGiraX[3]
		self.startVectorY = self.pointsMethodGiraY[3] 

	def shift(self):
		for i in range(3):
			self.pointsMethodGiraX[i] = self.pointsMethodGiraX[i+1]
			self.pointsMethodGiraY[i] = self.pointsMethodGiraY[i+1]

	def vectorHelper(self, function1, function2, w, v):
		resultVectorX = []
		resultVectorY = []
		x = self.startVectorX
		y = self.startVectorY
		a = self.step / self.a0 * eval(function1)
		b = self.a1 / self.a0 * self.pointsMethodGiraX[3]
		c = self.a2 / self.a0 * self.pointsMethodGiraX[2]
		d = self.a3 / self.a0 * self.pointsMethodGiraX[1]
		e = self.a4 / self.a0 * self.pointsMethodGiraX[0]
		resultVectorX = self.startVectorX - a + b + c + d + e
		a = self.step / self.a0 * eval(function2)
		b = self.a1 / self.a0 * self.pointsMethodGiraY[3]
		c = self.a2 / self.a0 * self.pointsMethodGiraY[2]
		d = self.a3 / self.a0 * self.pointsMethodGiraY[1]
		e = self.a4 / self.a0 * self.pointsMethodGiraY[0]
		resultVectorY = self.startVectorY - a + b + c + d + e
		return resultVectorX, resultVectorY

	def resultArray(self, function1, function2, w, v):
		vecX, vecY = self.vectorHelper(function1, function2, w, v)
		
		x = self.startVectorX
		y = self.startVectorY

		X1G = 1 - self.step / self.a0 * float(eval(str(self.dx1)))
		Y1G = (-1) * self.step / self.a0 * float(eval(str(self.dy1)))
		X2G = (-1) * self.step / self.a0 * float(eval(str(self.dx2)))
		Y2G = 1 - self.step / self.a0 * float(eval(str(self.dy2)))

		Determinate = X1G * Y2G - X2G * Y1G

		if Determinate == 0 :
			raise Exception("Not solution (Newton)")
		X1R = Y2G / Determinate 
		Y1R = (-1) * Y1G / Determinate 
		X2R = (-1) * X2G / Determinate 
		Y2R = X1G / Determinate

		new_x = self.startVectorX - (X1R * vecX + Y1R * vecY)
		new_y = self.startVectorY - (X2R * vecX + Y2R * vecY)

		if sqrt((abs(new_x - self.startVectorX)**2) + (abs(new_y - self.startVectorY))**2 ) >= self.eps:
			self.startVectorX = new_x
			self.startVectorY = new_y
			return self.resultArray(function1, function2, w, v)
		else:
			self.shift()
			self.startVectorX = new_x
			self.startVectorY = new_y
			self.resultX = new_x
			self.resultY = new_y
			self.pointsMethodGiraX[3] = new_x
			self.pointsMethodGiraY[3] = new_y
			return self.resultX, self.resultY

	def startComputing(self, function1, function2, w, v):
		self.getArrayPoints(function1, function2, w, v)
		resX=0
		resY=0
		x, y= symbols('x y')
		self.dx1 = diff(function1, x)
		self.dy1 = diff(function1, y)
		self.dx2 = diff(function2, x)
		self.dy2 = diff(function2, y)
		for i in range(4):
			self.PointGX.append( self.pointsMethodGiraX[i])
			self.PointGY.append( self.pointsMethodGiraY[i])
		for i in range(self.iteration - 4):
			resX,resY = self.resultArray(function1, function2, w, v)
			self.PointGX.append(resX)
			self.PointGY.append(resY)
		return self.PointGX, self.PointGY




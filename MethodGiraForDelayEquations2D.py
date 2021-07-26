from math import *
from MethodGiraNMForUser3D import *
from MethodRungeKuttaForUser3D import *
from MethodRungeKuttaMerson2D import *

class MethodGiraForDelayEquations2D():
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
		self.methodRunge = MethodRungeKutta4ForUser()
		self.methodRunge2 = MethodRungeKuttaMerson2D()
		self.startVectorX = 0
		self.startVectorY = 0
		self.pointsMethodGiraX = []
		self.pointsMethodGiraY = []
		self.resultX = 0
		self.resultY = 0
		self.PointGX = []
		self.PointGY = []
		self.eps = 0.01
		self.counter = 0
		self.time = 0
		#Для вычисленных значений
		self.dictionaryTime = {}
		# Для окружения
		self.dictionary = {}

	def setStep(self, step):
		self.methodRunge.setStep(step)
		self.methodRunge2.setStep(step)
		self.step = step 
	def setIter(self, iteration):
		self.iteration = iteration

	def dataFlowAssessment(self, function1, function2, startfunctionX, startfunctionY, **kwargs):
		flag = True
		for key, value in kwargs.items():
			if kwargs[key] != 0:
				flag = False
		if flag :
			MGN = MethodGiraNMForUser3D()
			MGN.methodRunge = self.methodRunge
			return MGN.startComputing(function1, function2, 0, 0, 0, 0)
		else :
			return self.startComputing(function1, function2, startfunctionX, startfunctionY, **kwargs)

	def getArrayPoints(self, function1, function2, startfunctionX, startfunctionY, **kwargs):
		self.methodRunge2.get4Point(function1, function2, startfunctionX, startfunctionY, **kwargs)
		self.dictionary = self.methodRunge2.dictionary
		self.dictionaryTime = self.methodRunge2.dictTime
		self.time = self.step*4
		self.pointsMethodGiraX = self.methodRunge2.arrayPointGiraX
		self.pointsMethodGiraY = self.methodRunge2.arrayPointGiraY
		self.startVectorX = self.pointsMethodGiraX[3]
		self.startVectorY = self.pointsMethodGiraY[3]

	def shift(self):
		for i in range(3):
			self.pointsMethodGiraX[i] = self.pointsMethodGiraX[i+1]
			self.pointsMethodGiraY[i] = self.pointsMethodGiraY[i+1]

	def vectorHelper(self, function1, function2, startfunctionX, startfunctionY, **kwargs):
		resultVectorX = []
		resultVectorY = []
		self.dictionary['x'] = self.startVectorX
		self.dictionary['y'] = self.startVectorY
		a = self.step / self.a0 * eval(function1, self.dictionary)
		b = self.a1 / self.a0 * self.pointsMethodGiraX[3]
		c = self.a2 / self.a0 * self.pointsMethodGiraX[2]
		d = self.a3 / self.a0 * self.pointsMethodGiraX[1]
		e = self.a4 / self.a0 * self.pointsMethodGiraX[0]
		resultVectorX = self.startVectorX - a + b + c + d + e
		a = self.step / self.a0 * eval(function2, self.dictionary)
		b = self.a1 / self.a0 * self.pointsMethodGiraY[3]
		c = self.a2 / self.a0 * self.pointsMethodGiraY[2]
		d = self.a3 / self.a0 * self.pointsMethodGiraY[1]
		e = self.a4 / self.a0 * self.pointsMethodGiraY[0]
		resultVectorY = self.startVectorY - a + b + c + d + e
		return resultVectorX, resultVectorY

	def resultArray(self, function1, function2, startfunctionX, startfunctionY, **kwargs):
		vecX, vecY = self.vectorHelper(function1, function2, startfunctionX, startfunctionY, **kwargs)
 
		self.dictionary['x'] = self.startVectorX
		self.dictionary['y'] = self.startVectorY

		X1G = 1 -self.step / self.a0 * float(eval(str(self.dx1), self.dictionary))
		Y1G = (-1) * self.step / self.a0 * float(eval(str(self.dy1), self.dictionary))
		X2G = (-1) * self.step / self.a0 * float(eval(str(self.dx2), self.dictionary))
		Y2G = 1 -self.step / self.a0 * float(eval(str(self.dy2), self.dictionary))

		Determinate = X1G * Y2G - X2G * Y1G
		if Determinate == 0 :
			raise Exception("Not solution (Newton)")

		#Коэффициенты обратной матрицы G
		X1R = Y2G / Determinate 
		Y1R = (-1) * Y1G / Determinate 
		X2R = (-1) * X2G / Determinate 
		Y2R = X1G / Determinate

		new_x = self.startVectorX - (X1R * vecX + Y1R * vecY)
		new_y = self.startVectorY - (X2R * vecX + Y2R * vecY)

		if sqrt((new_x - self.startVectorX)**2 + (new_y - self.startVectorY)**2 ) >= self.eps and self.counter < 100 :
			self.startVectorX = new_x
			self.startVectorY = new_y
			self.counter += 1
			return self.resultArray(function1, function2, startfunctionX, startfunctionY, **kwargs)
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

	def startComputing(self, function1, function2, startfunctionX, startfunctionY, **kwargs):
		self.getArrayPoints(function1, function2, startfunctionX, startfunctionY, **kwargs)
		resX=0
		resY=0
		x, y = symbols('x y')
		self.dx1 = diff(function1, x)
		self.dy1 = diff(function1, y)
		self.dx2 = diff(function2, x)
		self.dy2 = diff(function2, y)

		for i in range(4):
			self.PointGX.append( self.pointsMethodGiraX[i])
			self.PointGY.append( self.pointsMethodGiraY[i])

		for i in range(self.iteration - 4):
			for key, value in kwargs.items():
				if self.time - value > 0 :
					arrayPoints =  self.dictionaryTime.get(round(self.time - value, 10) )
					if key.find("alfa") != -1:
						self.dictionary[key] = arrayPoints[0]
					if key.find("beta") != -1:
						self.dictionary[key] = arrayPoints[1]
				else:
					t = self.time - value
					if key.find("alfa") != -1:
						self.dictionary[key]  = eval(startfunctionX, self.dictionary)
					if key.find("beta") != -1:
						self.dictionary[key]  = eval(startfunctionY, self.dictionary)

			#if(abs(resX) < 100000 and abs(resY) < 100000) :
			resX,resY = self.resultArray(function1, function2, startfunctionX, startfunctionY, **kwargs)
			self.PointGX.append(resX)
			self.PointGY.append(resY)
			self.dictionaryTime[round(self.time, 10)] = [resX, resY]
			self.time = self.time + self.step 
			self.dictionary['t'] = self.time

		return self.PointGX, self.PointGY



# k = MethodGiraForDelayEquations2D()
# k.setStep(0.01)
# k.dataFlowAssessment("0.1 * (1 - x) * x + 0.9 * (y - x) + 0.01*alfa1", "0.1 * (1 - y) * y + 0.9 * (x - y) + 0.01*beta1", "2 * sin(t)", "cos(t)", alfa1 = 2, beta1 = 2)
# print(k.PointGX)
# print(k.PointGY)
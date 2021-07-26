from math import *
from publicMethodRungeKutta import *
from sympy import *


""" Объединяет все прошлые методы. 
		Может вызываться вместо остальных методов"""

class MethodGiraGetResultCurva():
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
		self.methodRunge = MethodRungeKuttaGetResultCurva()
		self.startVectorX = 0.2
		self.startVectorY = 0.2
		self.startVectorZ = 0.2
		self.pointsMethodGiraT = [] 
		self.pointsMethodGiraX = []
		self.pointsMethodGiraY = []
		self.pointsMethodGiraZ = []
		self.PointGT = []
		self.PointGX = []
		self.PointGY = []
		self.PointGZ = []
		self.eps = 0.01
		self.counter = 0
		self.time = 0
		#Для вычисленных значений
		self.dictionaryTime = {}
		# Для окружения
		self.dictionary = {}

	def setStep(self, step):
		self.step = step

	def setStepDD(self, step):
		self.step = step
		self.methodRunge.setStep(step)

	def setIter(self, iteration):
		self.iteration = iteration

	def setStartPoint(self, x, y="", z=""):
		self.methodRunge.setStartPoint(x,y,z)

	def getArrayPoints(self, function1, function2, function3, startfunctionX, startfunctionY, startfunctionZ, **kwargs):
		self.methodRunge.startMethodRunge(function1, function2, function3, 4, startfunctionX, startfunctionY, startfunctionZ, **kwargs)
		self.dictionary = self.methodRunge.dictionary
		self.dictionaryTime = self.methodRunge.dictTime
		self.time = self.step*4
		self.pointsMethodGiraT = self.methodRunge.arrayPointRungeT
		self.pointsMethodGiraX = self.methodRunge.arrayPointRungeX
		self.pointsMethodGiraY = self.methodRunge.arrayPointRungeY
		self.pointsMethodGiraZ = self.methodRunge.arrayPointRungeZ
		self.startVectorX = self.pointsMethodGiraX[3]
		if function2 != "":
			self.startVectorY = self.pointsMethodGiraY[3]
		if function3 != "":
			self.startVectorZ = self.pointsMethodGiraZ[3]

	def shift(self, function1, function2, function3):
		for i in range(3):
			self.pointsMethodGiraT[i] = self.pointsMethodGiraT[i+1]
			self.pointsMethodGiraX[i] = self.pointsMethodGiraX[i+1]
			if function2 != "":
				self.pointsMethodGiraY[i] = self.pointsMethodGiraY[i+1]
			if function3 != "":
				self.pointsMethodGiraZ[i] = self.pointsMethodGiraZ[i+1]

	def vectorHelper(self, function1, function2, function3, startfunctionX, startfunctionY, startfunctionZ, **kwargs):
		resultVectorX = []
		resultVectorY = []
		resultVectorZ = []
		self.dictionary['t'] = self.time
		self.dictionary['x'] = self.startVectorX
		self.dictionary['y'] = self.startVectorY
		self.dictionary['z'] = self.startVectorZ
		if function1 != "":
			a = self.step / self.a0 * eval(function1, self.dictionary)
			b = self.a1 / self.a0 * self.pointsMethodGiraX[3]
			c = self.a2 / self.a0 * self.pointsMethodGiraX[2]
			d = self.a3 / self.a0 * self.pointsMethodGiraX[1]
			e = self.a4 / self.a0 * self.pointsMethodGiraX[0]
			resultVectorX = self.startVectorX - a + b + c + d + e
		if function2 != "":
			a = self.step / self.a0 * eval(function2, self.dictionary)
			b = self.a1 / self.a0 * self.pointsMethodGiraY[3]
			c = self.a2 / self.a0 * self.pointsMethodGiraY[2]
			d = self.a3 / self.a0 * self.pointsMethodGiraY[1]
			e = self.a4 / self.a0 * self.pointsMethodGiraY[0]
			resultVectorY = self.startVectorY - a + b + c + d + e
		if function3 != "":
			a = self.step / self.a0 * eval(function3, self.dictionary)
			b = self.a1 / self.a0 * self.pointsMethodGiraZ[3]
			c = self.a2 / self.a0 * self.pointsMethodGiraZ[2]
			d = self.a3 / self.a0 * self.pointsMethodGiraZ[1]
			e = self.a4 / self.a0 * self.pointsMethodGiraZ[0]
			resultVectorZ = self.startVectorZ - a + b + c + d + e
		return resultVectorX, resultVectorY, resultVectorZ

	def resultArray(self, function1, function2, function3, startfunctionX, startfunctionY, startfunctionZ, **kwargs):
		vecX, vecY, vecZ = self.vectorHelper(function1, function2, function3, startfunctionX, startfunctionY, startfunctionZ, **kwargs)
		new_x = 0
		new_y = 0
		new_z = 0
		self.dictionary['t'] = self.time
		self.dictionary['x'] = self.startVectorX
		self.dictionary['y'] = self.startVectorY
		self.dictionary['z'] = self.startVectorZ
		if function2 == "" and function3 == "":
			X1G = 1 -self.step / self.a0 * float(eval(str(self.dx1), self.dictionary))
			Determinate = 1
		elif function3 == "":
			X1G = 1 -self.step / self.a0 * float(eval(str(self.dx1), self.dictionary))
			Y1G = (-1) * self.step / self.a0 * float(eval(str(self.dy1), self.dictionary))
			X2G = (-1) * self.step / self.a0 * float(eval(str(self.dx2), self.dictionary))
			Y2G = 1 -self.step / self.a0 * float(eval(str(self.dy2), self.dictionary))
			Determinate = X1G * Y2G - X2G * Y1G
		else :
			X1G = 1 - self.step / self.a0 * float(eval(str(self.dx1), self.dictionary))
			Y1G = (-1) * self.step / self.a0 * float(eval(str(self.dy1), self.dictionary))
			Z1G = (-1) * self.step / self.a0 * float(eval(str(self.dz1), self.dictionary))
			X2G = (-1) * self.step / self.a0 * float(eval(str(self.dx2), self.dictionary))
			Y2G = 1 - self.step / self.a0 * float(eval(str(self.dy2), self.dictionary))
			Z2G = (-1) * self.step / self.a0 * float(eval(str(self.dz2), self.dictionary))
			X3G = (-1) * self.step / self.a0 * float(eval(str(self.dx3), self.dictionary))
			Y3G = (-1) * self.step / self.a0 * float(eval(str(self.dy3), self.dictionary))
			Z3G = 1 - self.step / self.a0 * float(eval(str(self.dz3), self.dictionary))
			Determinate = X1G * Y2G * Z3G + Y1G*Z2G*X3G + Z1G*X2G*Y3G - Z1G*Y2G*X3G - Y1G*X2G*Z3G - X1G*Z2G*Y3G

		if Determinate == 0 :
			raise Exception("Not solution (Newton)")

		if function2 != "" and function3 == "":
			#Коэффициенты обратной матрицы G
			X1R = Y2G / Determinate 
			Y1R = (-1) * Y1G / Determinate 
			X2R = (-1) * X2G / Determinate 
			Y2R = X1G / Determinate
		elif function3 != "":	
			#Коэффициенты обратной матрицы G
			X1R = (Y2G * Z3G - Z2G * Y3G) / Determinate 
			Y1R = (-1) * ( Y1G*Z3G -Z1G*Y3G ) / Determinate
			Z1R = (Y1G*Z2G - Y2G*Z1G) / Determinate

			X2R = (-1) * (X2G*Z3G - Z2G*X3G) / Determinate
			Y2R = (X1G*Z3G - Z1G*X3G) / Determinate
			Z2R = (-1) * (X1G * Z2G - Z1G * X2G) / Determinate

			X3R = (X2G * Y3G - Y2G * X3G) / Determinate
			Y3R = (-1) * (X1G * Y3G - Y1G*X3G) / Determinate 
			Z3R = (X1G * Y2G - Y1G * X2G) / Determinate

		fault = 0
		if function1 != "" and function2 == "" and function3 == "":
			new_x = self.startVectorX - vecX / X1G
			fault = abs(new_x - self.startVectorX)

		elif function1 != "" and function2 != "" and function3 == "":
			new_x = self.startVectorX - (X1R * vecX + Y1R * vecY)
			new_y = self.startVectorY - (X2R * vecX + Y2R * vecY)
			fault = ((abs(new_x - self.startVectorX))**2 + (abs(new_y - self.startVectorY))**2)**(1/2)

		elif function1 != "" and function2 != "" and function3 != "":
			new_x = self.startVectorX - (X1R * vecX + Y1R * vecY + Z1R * vecZ)
			new_y = self.startVectorY - (X2R * vecX + Y2R * vecY + Z2R * vecZ)
			new_z = self.startVectorZ - (X3R * vecX + Y3R * vecY + Z3R * vecZ)
			fault = ((abs(new_x - self.startVectorX))**2 + (abs(new_y - self.startVectorY))**2 + (abs((new_z - self.startVectorZ))**2))**(1/2)

		if  fault >= self.eps :
			self.startVectorX = new_x
			if function2 != "":
				self.startVectorY = new_y
			if function3 != "":
				self.startVectorZ = new_z
			return self.resultArray(function1, function2, function3, startfunctionX, startfunctionY, startfunctionZ, **kwargs)
		else:
			self.shift(function1, function2, function3)
			self.startVectorX = new_x
			self.pointsMethodGiraX[3] = new_x
			if function2 != "":
				self.startVectorY = new_y
				self.pointsMethodGiraY[3] = new_y
			if function3 != "":
				self.startVectorZ = new_z
				self.pointsMethodGiraZ[3] = new_z
			return new_x, new_y, new_z

	def startComputing(self, function1, function2, function3, startfunctionX, startfunctionY, startfunctionZ, **kwargs):
		self.getArrayPoints(function1, function2, function3, 
												startfunctionX, startfunctionY, startfunctionZ,
												**kwargs)
		resX=0
		resY=0
		resZ=0
		x, y, z = symbols('x y z')
		if function1 != "" and function2 == "" and function3 == "":
			self.dx1 = diff(function1, x)

		elif function1 != "" and function2 != "" and function3 == "":
			self.dx1 = diff(function1, x)
			self.dy1 = diff(function1, y)
			self.dx2 = diff(function2, x)
			self.dy2 = diff(function2, y)
			
		else:
			self.dx1 = diff(function1, x)
			self.dy1 = diff(function1, y)
			self.dz1 = diff(function1, z)
			self.dx2 = diff(function2, x)
			self.dy2 = diff(function2, y)
			self.dz2 = diff(function2, z)
			self.dx3 = diff(function3, x)
			self.dy3 = diff(function3, y)
			self.dz3 = diff(function3, z)

		for i in range(4):
			self.PointGT.append( self.pointsMethodGiraT[i])
			self.PointGX.append( self.pointsMethodGiraX[i])
			if function2 != "":
				self.PointGY.append( self.pointsMethodGiraY[i])
			if function3 != "":
				self.PointGZ.append( self.pointsMethodGiraZ[i])

		for i in range(self.iteration - 4):
			for key, value in kwargs.items():
				if key.find("alfa") == -1 and key.find("beta") == -1 and key.find("gamma") == -1:
					self.dictionary[key] = value
					continue
				if self.time - value > 0 :
					arrayPoints =  self.dictionaryTime.get(round(self.time - value, 10) )
					if key.find("alfa") != -1:
						self.dictionary[key] = arrayPoints[0]
					if key.find("beta") != -1:
						self.dictionary[key] = arrayPoints[1]
					if key.find("gamma") != -1:
						self.dictionary[key] = arrayPoints[2]
				else:
					t = self.time - value
					if key.find("alfa") != -1:
						self.dictionary[key]  = eval(startfunctionX)
					if key.find("beta") != -1:
						self.dictionary[key]  = eval(startfunctionY)
					if key.find("gamma") != -1:
						self.dictionary[key]  = eval(startfunctionZ)

			resX,resY,resZ = self.resultArray(function1, function2, function3, 
																				startfunctionX, startfunctionY, startfunctionZ, 
																				**kwargs)
			self.PointGT.append(self.time)
			self.PointGX.append(resX)
			if function2 != "":
				self.PointGY.append(resY)
			if function3 != "":
				self.PointGZ.append(resZ)
			if function1 != "" and function2 == "" and function3 == "":
				self.dictionaryTime[round(self.time, 10)] = [resX]
			elif function1 != "" and function2 != "" and function3 == "":
				self.dictionaryTime[round(self.time, 10)] = [resX, resY]
			else:
				self.dictionaryTime[round(self.time, 10)] = [resX, resY, resZ]
			self.time = self.time + self.step 
			self.dictionary['t'] = self.time

# m = MethodGiraGetResultCurva()
# m.setStepDD(0.001)
# #m.setStartPoint()
# m.setIter(4000)
# #m.startComputing("2*t - x + t*t", "", "", "", "", "")
# #m.startComputing("0.1 * (1 - x) * x + 0.9 * (y - x)", "0.1 * (1 - y) * y + 0.9 * (x - y)", "", "", "", "")
# #m.startComputing("y + w*z", "v*x*x - y", "1 - x", "", "", "", w =3.9, v = 0.9)
# #m.startComputing("w*(1 - v*alfa1 - (1 - v)*alfa2)*x", "", "", "3", "", "", w = 7.3, v = 0.2, alfa1 = 1, alfa2 = 0.3)
# m.startComputing("w*(1 - alfa1)*x + v*(y - x)", "w*(1 - beta1)*y + v*(x - y)", "", "2", "3", "", w = 6, v = 0.05, alfa1 = 1, beta1 = 1)
# #print(m.PointGT)
# print(m.PointGX)
# #print(m.PointGZ)
# #print(m.arrayPointRungeZ)
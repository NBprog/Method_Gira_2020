from math import *
from MethodGiraNMForUser3D import *
from MethodRungeKuttaForUser3D import *
from MethodRungeKuttaMerson3D import *

class MethodGiraForDelayEquations3D():
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
		self.methodRunge = MethodRungeKutta4ForUser3D()
		self.methodRunge2 = MethodRungeKuttaMerson3D()
		self.startVectorX = 0
		self.startVectorY = 0
		self.startVectorZ = 0 
		self.pointsMethodGiraX = []
		self.pointsMethodGiraY = []
		self.pointsMethodGiraZ = []
		self.resultX = 0
		self.resultY = 0
		self.resultZ = 0
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
		self.methodRunge.setStep(step)
		self.methodRunge2.setStep(step)
		self.step = step 
	def setIter(self, iteration):
		self.iteration = iteration

	def dataFlowAssessment(self, function1, function2, function3, startfunctionX, startfunctionY, startfunctionZ, **kwargs):
		flag = True
		for key, value in kwargs.items():
			if kwargs[key] != 0:
				flag = False
		if flag :
			MGN = MethodGiraNMForUser3D()
			MGN.methodRunge = self.methodRunge
			return MGN.startComputing(function1, function2, function3, 0, 0, 0, 0)
		else :
			return self.startComputing(function1, function2, function3, startfunctionX, startfunctionY, startfunctionZ, **kwargs)

	def getArrayPoints(self, function1, function2, function3, startfunctionX, startfunctionY, startfunctionZ, **kwargs):
		self.methodRunge2.get4Point(function1, function2, function3, startfunctionX, startfunctionY, startfunctionZ, **kwargs)
		self.dictionary = self.methodRunge2.dictionary
		self.dictionaryTime = self.methodRunge2.dictTime
		self.time = self.step*4
		self.pointsMethodGiraX = self.methodRunge2.arrayPointGiraX
		self.pointsMethodGiraY = self.methodRunge2.arrayPointGiraY
		self.pointsMethodGiraZ = self.methodRunge2.arrayPointGiraZ
		self.startVectorX = self.pointsMethodGiraX[3]
		self.startVectorY = self.pointsMethodGiraY[3]
		self.startVectorZ = self.pointsMethodGiraZ[3]

	def shift(self):
		for i in range(3):
			self.pointsMethodGiraX[i] = self.pointsMethodGiraX[i+1]
			self.pointsMethodGiraY[i] = self.pointsMethodGiraY[i+1]
			self.pointsMethodGiraZ[i] = self.pointsMethodGiraZ[i+1]

	def vectorHelper(self, function1, function2, function3, startfunctionX, startfunctionY, startfunctionZ, **kwargs):
		resultVectorX = []
		resultVectorY = []
		resultVectorZ = []
		self.dictionary['x'] = self.startVectorX
		self.dictionary['y'] = self.startVectorY
		self.dictionary['z'] = self.startVectorZ
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
		a = self.step / self.a0 * eval(function3, self.dictionary)
		b = self.a1 / self.a0 * self.pointsMethodGiraZ[3]
		c = self.a2 / self.a0 * self.pointsMethodGiraZ[2]
		d = self.a3 / self.a0 * self.pointsMethodGiraZ[1]
		e = self.a4 / self.a0 * self.pointsMethodGiraZ[0]
		resultVectorZ = self.startVectorZ - a + b + c + d + e
		return resultVectorX, resultVectorY, resultVectorZ

	def resultArray(self, function1, function2, function3, startfunctionX, startfunctionY, startfunctionZ, **kwargs):
		vecX, vecY, vecZ = self.vectorHelper(function1, function2, function3, startfunctionX, startfunctionY, startfunctionZ, **kwargs)
 
		self.dictionary['x'] = self.startVectorX
		self.dictionary['y'] = self.startVectorY
		self.dictionary['z'] = self.startVectorZ

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

		new_x = self.startVectorX - (X1R * vecX + Y1R * vecY + Z1R * vecZ)
		new_y = self.startVectorY - (X2R * vecX + Y2R * vecY + Z2R * vecZ)
		new_z = self.startVectorZ - (X3R * vecX + Y3R * vecY + Z3R * vecZ)

		if ((abs(new_x - self.startVectorX))**2 + (abs(new_y - self.startVectorY))**2 + (abs((new_z - self.startVectorZ))**2))**(1/2) >= self.eps and self.counter < 100 :
			self.startVectorX = new_x
			self.startVectorY = new_y
			self.startVectorZ = new_z
			self.counter += 1
			return self.resultArray(function1, function2, function3, startfunctionX, startfunctionY, startfunctionZ, **kwargs)
		else:
			self.shift()
			self.startVectorX = new_x
			self.startVectorY = new_y
			self.startVectorZ = new_z
			if self.counter < 100 :
				self.resultX = new_x
				self.resultY = new_y
				self.resultZ = new_z
			self.counter = 0
			self.pointsMethodGiraX[3] = new_x
			self.pointsMethodGiraY[3] = new_y
			self.pointsMethodGiraZ[3] = new_z
			return self.resultX, self.resultY, self.resultZ

	def startComputing(self, function1, function2, function3, startfunctionX, startfunctionY, startfunctionZ, **kwargs):
		self.getArrayPoints(function1, function2, function3, startfunctionX, startfunctionY, startfunctionZ, **kwargs)
		resX=0
		resY=0
		resZ=0
		x, y, z = symbols('x y z')
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
			self.PointGX.append( self.pointsMethodGiraX[i])
			self.PointGY.append( self.pointsMethodGiraY[i])
			self.PointGZ.append( self.pointsMethodGiraZ[i])

		for i in range(self.iteration - 4):
			for key, value in kwargs.items():
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
			if(abs(resX) < 100000 and abs(resY) < 100000 and abs(resZ) < 100000) :
				resX,resY,resZ = self.resultArray(function1, function2, function3, startfunctionX, startfunctionY, startfunctionZ, **kwargs)
			self.PointGX.append(resX)
			self.PointGY.append(resY)
			self.PointGZ.append(resZ)
			self.dictionaryTime[round(self.time, 10)] = [resX, resY, resZ]
			self.time = self.time + self.step 

		return self.PointGX, self.PointGY, self.PointGZ



#x=0
#y=0
#z=0
#k = MethodGiraForDelayEquations()
#k.setStep(0.01)
#try:
#x,y,z = k.dataFlowAssessment("y + 3.9*z + 0.001*alfa1", "0.9*x*x - y + 0.0001*beta1", "1 - x + 0.1*gamma1", "2 * sin(t)", "cos(t)", "sin(cos(t))", alfa1 = 2, beta1 = 2, gamma1 = 2)
#x,y,z = k.dataFlowAssessment("y + 3.9*z", "0.9*x*x - y", "1 - x ", "2 * sin(t)", "cos(t)", "sin(cos(t))", alfa1 = 0, beta1 = 0, gamma1 = 0)
#except Exception:
#	print('Это что ещё такое?')
#print(x)
#print(y)
#print(z)





























# def function1(t, x, y):
# 	return 2.7*y + z
# def function2(t, x, y):
# 	return 0.1 * (1 - y) * y + 0.9 * (x - y)



# k = MethodGiraForDelayEquations()
# #a_dict = {'color': 1, 'fruit': 2, 'pet': 3}
# a = 0
# b = 0
# c = 0 
# x, y, z = k.dataFlowAssessment("2.7*y + z","-x + y*y", "x + y", a = 0, b = 0, c = 0)
# print(x)
# print(y)
# print(z)

# a_dict = {'color': 1, 'fruit': 2, 'pet': 3}

# for key, value in a_dict.items():
# 	a_dict[key] = value + 1

# print(a_dict)


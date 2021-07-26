from MethodRungeKutta import *
from math import cos, sin, sqrt, e, pi, pow
from SystemODY import *


""" Объединяет все прошлые методы. 
		Может вызываться вместо остальных методов"""
		
class MethodRungeKuttaGetResultCurva():
	def __init__(self):
		self.iteration = 1000
		self.step = 0.0001
		self.startX = 0.2
		self.startY = 0.2
		self.startZ = 0.2
		self.time = 0
		self.eps = 0.0001
		self.arrayPointRungeT = []
		self.arrayPointRungeX = []
		self.arrayPointRungeY = []
		self.arrayPointRungeZ = []
		self.dictionary = {'alfa1' : 0, 'alfa2' : 0, 'alfa3' : 0, 'beta1' : 0, 'beta2' : 0, 'beta3' : 0, 'gamma1' : 0, 'gamma2' : 0, 'gamma3' : 0}
		self.dictTime = {}
		self.cos = cos
		self.sin = sin
		self.sqrt = sqrt
		self.e = e
		self.pi = pi
		self.pow = pow

	def setStep(self,step):
		self.step = step
	def setIter(self, iteration):
		self.iteration = iteration
	def setStartPoint(self, x, y="", z=""):
		self.startX = x
		if y != "" :
			self.startY = y
		if z != "" :
			self.startZ = z

	def startMethodRunge(self, function1, function2, function3, iteration, startFunctionX, startFunctionY, startFunctionZ, **kwargs):
		self.dictionary["cos"] = self.cos
		self.dictionary["sin"] = self.sin
		self.dictionary["sqrt"] = self.sqrt
		self.dictionary["e"] = self.e
		self.dictionary["pi"] = self.pi
		self.dictionary["pow"] = self.pow

		if iteration == "":
			iteration = self.iteration 

		for i in range(iteration):
			for key, value in kwargs.items():
				if key.find("alfa") == -1 and key.find("beta") == -1 and key.find("gamma") == -1:
					self.dictionary[key] = value
					continue
				if self.time - value > 0 :
					arrayPoints =  self.dictTime.get(round(self.time - value, 10) )
					if key.find("alfa") != -1:
						self.dictionary[key] = arrayPoints[0]
					if key.find("beta") != -1:
						self.dictionary[key] = arrayPoints[1]
					if key.find("gamma") != -1:
						self.dictionary[key] = arrayPoints[2]
				else:
					t = self.time - value
					if key.find("alfa") != -1:
						self.dictionary[key]  = eval(startFunctionX)
					if key.find("beta") != -1:
						self.dictionary[key]  = eval(startFunctionY)
					if key.find("gamma") != -1:
						self.dictionary[key]  = eval(startFunctionZ)

			if i == 0 and startFunctionX != "":
				t = self.time
				self.startX = eval(startFunctionX)
				if startFunctionY != "" :
					self.startY = eval(startFunctionY)
				if startFunctionZ != "" :
					self.startZ = eval(startFunctionZ)
			# Задание начальных данных 
			self.dictionary['x'] = self.startX
			self.dictionary['t'] = self.time
			if function2 != "" :
				self.dictionary['y'] = self.startY
			if function3 != "" :
				self.dictionary['z'] = self.startZ
			# Расчёт коэффициентов
			k1x = eval(function1, self.dictionary)
			if function2 != "" :
				k1y = eval(function2, self.dictionary)
			if function3 != "" :
				k1z = eval(function3, self.dictionary)

			self.dictionary['x'] = self.startX + k1x * self.step / 2
			self.dictionary['t'] = self.time + self.step / 2
			if function2 != "" :
				self.dictionary['y'] = self.startY + k1y * self.step / 2
			if function3 != "" :
				self.dictionary['z'] = self.startZ + k1z * self.step / 2

			k2x = eval(function1, self.dictionary)
			if function2 != "" : 
				k2y = eval(function2, self.dictionary)
			if function3 != "" :
				k2z = eval(function3, self.dictionary)

			self.dictionary['x'] = self.startX + k2x * self.step / 2
			self.dictionary['t'] = self.time + self.step / 2
			if function2 != "" :
				self.dictionary['y'] = self.startY + k2y * self.step / 2
			if function3 != "" :
				self.dictionary['z'] = self.startZ + k2z * self.step / 2

			k3x = eval(function1, self.dictionary)
			if function2 != "" :
				k3y = eval(function2, self.dictionary)
			if function3 != "" :	
				k3z = eval(function3, self.dictionary)

			self.dictionary['x'] = self.startX + k3x * self.step
			self.dictionary['t'] = self.time + self.step
			if function2 != "" :
				self.dictionary['y'] = self.startY + k3y * self.step
			if function3 != "" :
				self.dictionary['z'] = self.startZ + k3z * self.step

			k4x = eval(function1, self.dictionary)
			if function2 != "" :
				k4y = eval(function2, self.dictionary)
			if function3 != "" :
				k4z = eval(function3, self.dictionary)
			# Добавление вычисленных данных в массив 
			self.arrayPointRungeX.append(self.startX)
			self.arrayPointRungeT.append(self.time)
			if function2 != "" :
				self.arrayPointRungeY.append(self.startY)
			if function3 != "" :
				self.arrayPointRungeZ.append(self.startZ)
			if function1 != "" and function2 != "" and function3 != "":
				self.dictTime[round(self.time, 10)] = [self.startX, self.startY, self.startZ]
			elif function1 != "" and function2 != "" and function3 == "":
				self.dictTime[round(self.time, 10)] = [self.startX, self.startY]
			elif function1 != "" and function2 == "" and function3 == "":
				self.dictTime[round(self.time, 10)] = [self.startX]
			# Получение нового значения  
			self.startX += self.result(k1x, k2x, k3x, k4x)
			self.time += self.step
			if function2 != "" :
				self.startY += self.result(k1y, k2y, k3y, k4y)
			if function3 != "" :
				self.startZ += self.result(k1z, k2z, k3z, k4z)

	# Функция возвращающая приращение 
	def result(self, k1, k2, k3, k4):
		return self.step / 6 * (k1 + 2*k2 + 2*k3 + k4)


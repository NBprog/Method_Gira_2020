from SystemODY import *

class SystemODY4(SystemODY) :
	def __init__(self, step = 0.1, a0 = 25/12, a1 = -4, a2 = 3, a3 = -4/3, a4 =1/4):
		self.step = step
		self.a0 = a0
		self.a1 = a1
		self.a2 = a2
		self.a3 = a3
		self.a4 = a4

	def setStep(self, step):
		self.step = step 

	def function1(self, x, y):
		return y

	def function2(self, x ,y):
		return 4*(1-x*x)*y - x

	#Задание матрицы производных функции 

	def DxFunction1(self, x, y):
		return 0

	def DyFunction1(self, x, y):
		return 1

	def DxFunction2(self, x, y):
		return -2*4*x*y-1

	def DyFunction2(self, x ,y):
		return 4 - 4*x*x

	def GetFunction1(self):
		return "y"
		
	def GetFunction2(self):
		return "4*(1- x*x)*y - x"
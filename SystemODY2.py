from SystemODY import *

class SystemODY2(SystemODY) :
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
		return x*x - y - 2*x

	#Задание матрицы производных функции 

	def DxFunction1(self, x, y):
		return 0

	def DyFunction1(self, x, y):
		return 1

	def DxFunction2(self, x, y):
		return 2*x - 2

	def DyFunction2(self, x ,y):
		return -1

	def GetFunction1(self):
		return "y"
		
	def GetFunction2(self):
		return "x^2 - y - 2*x"


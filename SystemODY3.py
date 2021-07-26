from SystemODY import *

class SystemODY3(SystemODY) :
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
		return 3*x - 4*y
		
	def function2(self, x ,y):
		return 2*x - y

	#Задание матрицы производных функции 

	def DxFunction1(self, x, y):
		return 3

	def DyFunction1(self, x, y):
		return -4

	def DxFunction2(self, x, y):
		return 2

	def DyFunction2(self, x ,y):
		return -1

	def GetFunction1(self):
		return "3*x - 4*y"

	def GetFunction2(self):
		return "2*x - y"
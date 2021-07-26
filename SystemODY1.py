from SystemODY import *

class SystemODY1(SystemODY) :
	def __init__(self, step = 0.1, a0 = 25/12, a1 = -4, a2 = 3, a3 = -4/3, a4 =1/4):
		self.a0 = a0
		self.a1 = a1
		self.a2 = a2
		self.a3 = a3
		self.a4 = a4
		self.step = step

	def setStep(self, step):
		self.step = step

	def function1(self, x, y):
		return -x

	def function2(self, x, y):
		return 2*x-2*y

	#Задание матрицы производных функции
	def DxFunction1(self, x, y):
		return -1

	def DyFunction1(self, x ,y):
		return 0

	def DxFunction2(self, x, y):
		return 2

	def DyFunction2(self, x, y):
		return -2

	def GetFunction1(self):
		return "-x"
		
	def GetFunction2(self):
		return "2*x-2*y"



# x = 2
# y = 3
# k = SystemODY1()
# print(k.X1ReverseG(x,y))
# print(k.Y1ReverseG(x,y))
# print(k.X2ReverseG(x,y))
# print(k.Y2ReverseG(x,y))

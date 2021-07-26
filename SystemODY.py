class SystemODY :
	def __init__(self, step=0.1, a0 = 25/12, a1 = -4, a2 = 3, a3 = -4/3, a4 =1/4):
		self.a0 = a0
		self.a1 = a1
		self.a2 = a2
		self.a3 = a3
		self.a4 = a4
		self.step = step

	def setStep(self, step):
		self.step = step

	def function1(self, x, y):
		return 0.1 * (1 - x) * x + 0.9 * (y -x)

	def function2(self, x, y):
		return 0.1 * (1 - y) * y + 0.9 * (x -y)

	def DxFunction1(self, x, y):
		return -0.2*x -0.8

	def DyFunction1(self, x, y):
		return 0.9

	def DxFunction2(self, x, y):
		return 0.9

	def DyFunction2(self, x, y):
		return -0.2*y - 0.8

	def GetFunction1(self):
		return "0.1 * (1 - x) * x + 0.9 * (y - x)"

	def GetFunction2(self):
		return "0.1 * (1 - y) * y + 0.9 * (x - y)"
		
	# Нахождение определителя матрицы Якоби
	def Determinate(self, x, y):
		det = self.X1Gmatrix(x, y) * self.Y2Gmatrix(x, y) - self.X2Gmatrix(x,y) * self.Y1Gmatrix(x, y)
		if det == 0:
			raise Exception("Not solution")
		return det

	def X1Gmatrix(self, x, y) :
		return 1 - self.step / self.a0 * self.DxFunction1(x, y)

	def Y1Gmatrix(self, x, y) :
		return (-1) * self.step / self.a0 * self.DyFunction1(x, y)

	def X2Gmatrix(self, x, y) :
		return (-1) * self.step / self.a0 * self.DxFunction2(x, y)

	def Y2Gmatrix(self, x, y) :
		return 1 - self.step / self.a0 * self.DyFunction2(x, y)

	def X1ReverseG(self, x, y):
		return self.Y2Gmatrix(x, y)

	def Y1ReverseG(self, x, y):
		return (-1) * self.Y1Gmatrix(x, y) / self.Determinate(x, y)

	def X2ReverseG(self, x, y):
		return (-1) * self.X2Gmatrix(x, y) / self.Determinate(x, y)

	def Y2ReverseG(self, x ,y):
		return self.X1Gmatrix(x ,y) / self.Determinate(x, y)



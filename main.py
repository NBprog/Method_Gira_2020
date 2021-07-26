import sys 
import time 

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from Gir import Ui_MainWindow
from SystemODY import *
from SystemODY1 import *
from SystemODY2 import *
from SystemODY3 import *
from SystemODY4 import *
from MethodGiraNM import *
from MethodRKODY import *
from MethodGNODY import *
from MethodGiraNMForUser import *
from MethodGiraNMForUser3D import *
from MethodGiraSIM import *
from MethodRungeKutta import *
from MethodRungeKuttaForUser import *
from MethodRungeKuttaForUser3D import *
from MethodRungeKuttaMerson2D import *
from MethodRungeKuttaMerson3D import *
from MethodGiraForDelayEquations2D import *
from MethodGiraForDelayEquations3D import *
from TestingMethod import *

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None, *args, **kwargs):
		QMainWindow.__init__(self)
		self.setupUi(self)


def is_digit(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

def sixth_button(main):
    try:
        count_row = 1000
        MRK = MethodRKODY()
        MGN = MethodGNODY()

        alfa1 = 1
        alfa2 = 1
        alfa3 = 1
        w = 1

        if main.stepddy.text() != "" :
            if is_digit(main.stepddy.text()) :
                MRK.setStep(float(main.stepddy.text()))
                MGN.setStep(float(main.stepddy.text()))
            else:
                raise ValueError("Enter the number!")

        if main.Iterddy.text() != "" :
            if main.Iterddy.text().isdigit():
                count_row = int(main.Iterddy.text())
                MRK.setIter(int(main.Iterddy.text()))
                MGN.setIter(int(main.Iterddy.text()))
            else:
                raise ValueError("Enter the number!")

        if main.alfa1ddy.text() != "" :
            if is_digit(main.alfa1ddy.text()):
                alfa1 = float(main.alfa1ddy.text())
            else:
                raise ValueError("Enter the number!")

        if main.alfa2ddy.text() != "" :
            if is_digit(main.alfa2ddy.text()):
                alfa2 = float(main.alfa2ddy.text())
            else:
                raise ValueError("Enter the number!")

        if main.alfa3ddy.text() != "" :
            if is_digit(main.alfa3ddy.text()):
                alfa3 = float(main.alfa3ddy.text())
            else:
                raise ValueError("Enter the number!")

        if main.helperW.text() != "" :
            if is_digit(main.helperW.text()):
                w = float(main.helperW.text())
            else:
                raise ValueError("Enter the number!")

        if main.Sys1Ddy.text() == "" :
            return  

        if main.InitFunc1.text() == "" :
            return

        function1 = main.Sys1Ddy.text()

        startfunctionX = main.InitFunc1.text()

        MRK.startMethodRunge(function1, startfunctionX, 
                             alfa1 = alfa1, alfa2 = alfa2,
                             alfa3 = alfa3, w = w)
        
        x, t = MGN.startComputing(function1, startfunctionX, 
                                  alfa1 = alfa1, alfa2 = alfa2, alfa3 = alfa3, 
                                  w = w)

        fig = Figure()
        axes = fig.add_subplot(111)
        axes.plot(MRK.arrayPointRungeT, MRK.arrayPointRungeX, label='MethodRungeKutta')
        axes.plot(t, x, label = 'MethodGiraNewton')
        axes.set_xlabel('time')
        axes.yaxis.set_label_position("right")
        axes.set_ylabel('     x', rotation = 0)
        axes.legend()
        main.canavas6 = MyMplCanavas(fig)
        for i in reversed(range(main.componovka6.count())): 
            main.componovka6.itemAt(i).widget().deleteLater()
        main.componovka6.addWidget(main.canavas6)
        main.toolbar6 = NavigationToolbar(main.canavas6, main)
        main.componovka6.addWidget(main.toolbar6)

        main.tableWidget_5.setColumnCount(4)
        main.tableWidget_5.setRowCount(count_row)
        main.tableWidget_5.setHorizontalHeaderLabels(["MethodRungeKuttaTime", 
                                                      "MethodRungeKuttaX",
                                                      "MethodGiraNewtonTime", 
                                                      "MethodGiraNewtonX"])

        for i in range(count_row):
            main.tableWidget_5.setItem(i, 0 , QTableWidgetItem(str(MRK.arrayPointRungeT[i])) )
            main.tableWidget_5.setItem(i, 1 , QTableWidgetItem(str(MRK.arrayPointRungeX[i])) )
            main.tableWidget_5.setItem(i, 2 , QTableWidgetItem(str(t[i])) )
            main.tableWidget_5.setItem(i, 3 , QTableWidgetItem(str(x[i])) )

        main.tableWidget_5.resizeColumnsToContents()
    except ValueError :
        QMessageBox.about(main, "Warning", "Please enter a real number in the field!")
    except Exception:
        QMessageBox.about(main, "Warning", "Please check your entries. Something went wrong...")

def fifth_button(main):
    try:
        count_row = 1000
        MRK = MethodRungeKuttaMerson3D()
        MGN = MethodGiraForDelayEquations3D()

        alfa1 = 1
        alfa2 = 1
        alfa3 = 1
        beta1 = 1
        beta2 = 1
        beta3 = 1
        gamma1 = 1
        gamma2 = 1
        gamma3 = 1

        if main.stepddy3D.text() != "" :
            if is_digit(main.stepddy3D.text()) :
                MRK.setStep(float(main.stepddy3D.text()))
                MGN.setStep(float(main.stepddy3D.text()))
            else:
                raise ValueError("Enter the number!")

        if main.Iterddy3D.text() != "" :
            if main.Iterddy3D.text().isdigit():
                count_row = int(main.Iterddy3D.text())
                MRK.setIter(int(main.Iterddy3D.text()))
                MGN.setIter(int(main.Iterddy3D.text()))
            else:
                raise ValueError("Enter the number!")

        if main.alfa13D.text() != "" :
            if is_digit(main.alfa13D.text()):
                alfa1 = float(main.alfa13D.text())
            else:
                raise ValueError("Enter the number!")

        if main.alfa23D.text() != "" :
            if is_digit(main.alfa23D.text()):
                alfa2 = float(main.alfa23D.text())
            else:
                raise ValueError("Enter the number!")

        if main.alfa33D.text() != "" :
            if is_digit(main.alfa33D.text()):
                alfa3 = float(main.alfa33D.text())
            else:
                raise ValueError("Enter the number!")

        if main.beta13D.text() != "" :
            if is_digit(main.beta13D.text()):
                beta1 = float(main.beta13D.text())
            else:
                raise ValueError("Enter the number!")

        if main.beta23D.text() != "" :
            if is_digit(main.beta23D.text()):
                beta2 = float(main.beta23D.text())
            else:
                raise ValueError("Enter the number!")

        if main.beta33D.text() != "" :
            if is_digit(main.beta33D.text()):
                beta3 = float(main.beta33D.text())
            else:
                raise ValueError("Enter the number!")

        if main.gamma13D.text() != "" :
            if is_digit(main.gamma13D.text()):
                gamma1 = float(main.gamma13D.text())
            else:
                raise ValueError("Enter the number!")

        if main.gamma23D.text() != "" :
            if is_digit(main.gamma23D.text()):
                gamma2 = float(main.gamma23D.text())
            else:
                raise ValueError("Enter the number!")

        if main.gamma33D.text() != "" :
            if is_digit(main.gamma33D.text()):
                beta3 = float(main.gamma33D.text())
            else:
                raise ValueError("Enter the number!")

        if main.Sys1Ddy3D.text() == "" or main.Sys2Ddy3D.text() == "" or main.Sys3Ddy3D.text() == "" :
            return  

        if main.InitFunc13D.text() == "" or main.InitFunc23D.text() == "" or main.InitFunc33D.text() == "" :
            return

        function1 = main.Sys1Ddy3D.text()
        function2 = main.Sys2Ddy3D.text()
        function3 = main.Sys3Ddy3D.text()

        startfunctionX = main.InitFunc13D.text()
        startfunctionY = main.InitFunc23D.text()
        startfunctionZ = main.InitFunc33D.text()

        MRK.startMethodRunge(function1, function2, function3, 
                             startfunctionX, startfunctionY, startfunctionZ, 
                             alfa1 = alfa1, alfa2 = alfa2, alfa3 = alfa3,
                             beta1 = beta1, beta2 = beta2, beta3 = beta3,
                             gamma1 = gamma1, gamma2 = gamma2, gamma3 = gamma3)

        x, y, z = MGN.dataFlowAssessment(function1, function2, function3, 
                                         startfunctionX, startfunctionY, startfunctionZ, 
                                         alfa1 = alfa1, alfa2 = alfa2, alfa3 = alfa3, 
                                         beta1 = beta1, beta2 = beta2, beta3 = beta3, 
                                         gamma1 = gamma1, gamma2 = gamma2, gamma3 = gamma3)

        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.plot3D(MRK.arrayPointRungeX, MRK.arrayPointRungeY, MRK.arrayPointRungeZ, label='MethodRungeKutta', color = 'b')
        ax.plot3D(x, y, z, label = 'MethodGiraNewton', color = 'g')
        #ax.plot3D(MRK.arrayPointRungeX, MRK.arrayPointRungeY, MRK.arrayPointRungeZ)
        #ax.plot3D(x, y, z)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        ax.legend()
        plt.show()
        main.canavas5 = MyMplCanavas(fig)
        for i in reversed(range(main.componovka5.count())): 
            main.componovka5.itemAt(i).widget().deleteLater()
        main.componovka5.addWidget(main.canavas5)
        main.toolbar5 = NavigationToolbar(main.canavas5, main)
        main.componovka5.addWidget(main.toolbar5)

        main.tableWidget_3.setColumnCount(6)
        main.tableWidget_3.setRowCount(count_row)
        main.tableWidget_3.setHorizontalHeaderLabels(["MethodRungeKuttaX", "MethodRungeKuttaY", 
                                                      "MethodRungeKuttaZ", "MethodGiraNewtonX",
                                                      "MethodGiraNewtonY", "MethodGiraNewtonZ"])

        for i in range(count_row):
            main.tableWidget_3.setItem(i, 0 , QTableWidgetItem(str(MRK.arrayPointRungeX[i])) )
            main.tableWidget_3.setItem(i, 1 , QTableWidgetItem(str(MRK.arrayPointRungeY[i])) )
            main.tableWidget_3.setItem(i, 2 , QTableWidgetItem(str(MRK.arrayPointRungeZ[i])) )
            main.tableWidget_3.setItem(i, 3 , QTableWidgetItem(str(x[i])) )
            main.tableWidget_3.setItem(i, 4 , QTableWidgetItem(str(y[i])) )
            main.tableWidget_3.setItem(i, 5 , QTableWidgetItem(str(z[i])) )

        main.tableWidget_3.resizeColumnsToContents()

    except ValueError :
        QMessageBox.about(main, "Warning", "Please enter a real number in the field!")
    except Exception:
        QMessageBox.about(main, "Warning", "Please check your entries. Something went wrong...")    

def fourth_button(main):
    try:
        count_row = 1000
        MRK = MethodRungeKuttaMerson2D()
        MGN = MethodGiraForDelayEquations2D()
        MRK4 = MethodRungeKutta2D()

        alfa1 = 1
        alfa2 = 1
        alfa3 = 1
        beta1 = 1
        beta2 = 1
        beta3 = 1
        w = 1
        v = 1

        if main.stepddy2D.text() != "" :
            if is_digit(main.stepddy2D.text()) :
                MRK.setStep(float(main.stepddy2D.text()))
                MRK4.setStep(float(main.stepddy2D.text()))
                MGN.setStep(float(main.stepddy2D.text()))
            else:
                raise ValueError("Enter the number!")

        if main.Iterddy2D.text() != "" :
            if main.Iterddy2D.text().isdigit():
                count_row = int(main.Iterddy2D.text())
                MRK.setIter(int(main.Iterddy2D.text()))
                MRK4.setIter(int(main.Iterddy2D.text()))
                MGN.setIter(int(main.Iterddy2D.text()))
            else:
                raise ValueError("Enter the number!")

        if main.alfa12D.text() != "" :
            if is_digit(main.alfa12D.text()):
                alfa1 = float(main.alfa12D.text())
            else:
                raise ValueError("Enter the number!")

        if main.alfa22D.text() != "" :
            if is_digit(main.alfa22D.text()):
                alfa2 = float(main.alfa22D.text())
            else:
                raise ValueError("Enter the number!")

        if main.alfa32D.text() != "" :
            if is_digit(main.alfa32D.text()):
                alfa3 = float(main.alfa32D.text())
            else:
                raise ValueError("Enter the number!")

        if main.beta12D.text() != "" :
            if is_digit(main.beta12D.text()):
                beta1 = float(main.beta12D.text())
            else:
                raise ValueError("Enter the number!")

        if main.beta22D.text() != "" :
            if is_digit(main.beta22D.text()):
                beta2 = float(main.beta22D.text())
            else:
                raise ValueError("Enter the number!")

        if main.beta32D.text() != "" :
            if is_digit(main.beta32D.text()):
                beta3 = float(main.beta32D.text())
            else:
                raise ValueError("Enter the number!")

        if main.helperW2.text() != "" :
            if is_digit(main.helperW2.text()):
                w = float(main.helperW2.text())
            else:
                raise ValueError("Enter the number!")

        if main.helperV2.text() != "" :
            if is_digit(main.helperV2.text()):
                v = float(main.helperV2.text())
            else:
                raise ValueError("Enter the number!")

        if main.Sys1Ddy2D.text() == "" or main.Sys2Ddy2D.text() == "" :
            return  

        if main.InitFunc12D.text() == "" or main.InitFunc22D.text() == "" :
            return

        function1 = main.Sys1Ddy2D.text()
        function2 = main.Sys2Ddy2D.text()

        startfunctionX = main.InitFunc12D.text()
        startfunctionY = main.InitFunc22D.text()

        MRK.startMethodRunge(function1, function2, startfunctionX, startfunctionY, 
                             alfa1 = alfa1, alfa2 = alfa2, alfa3 = alfa3, 
                             beta1 = beta1, beta2 = beta2, beta3 = beta3, 
                             w = w, v = v)

        MRK4.startMethodRunge(function1, function2, 
                              startfunctionX, startfunctionY, 
                              alfa1 = alfa1, alfa2 = alfa2, alfa3 = alfa3,
                              beta1 = beta1, beta2 = beta2, beta3 = beta3,
                              w = w, v = v)

        x, y = MGN.dataFlowAssessment(function1, function2, 
                                      startfunctionX, startfunctionY,
                                      alfa1 = alfa1, alfa2 = alfa2, alfa3 = alfa3, 
                                      beta1 = beta1, beta2 = beta2, beta3 = beta3, 
                                      w = w, v = v)

        fig = Figure()
        axes = fig.add_subplot(111)
        axes.plot(MRK.arrayPointRungeX, MRK.arrayPointRungeY, label='MethodRungeKuttaMerson')
        axes.plot(MRK.arrayPointRungeX, MRK.arrayPointRungeY, label='MethodRungeKutta4')
        axes.plot(x, y, label = 'MethodGiraNewton')
        axes.set_xlabel('x')
        axes.yaxis.set_label_position("right")
        axes.set_ylabel('     y', rotation = 0)
        axes.legend()
        main.canavas4 = MyMplCanavas(fig)
        for i in reversed(range(main.componovka4.count())): 
            main.componovka4.itemAt(i).widget().deleteLater()
        main.componovka4.addWidget(main.canavas4)
        main.toolbar4 = NavigationToolbar(main.canavas4, main)
        main.componovka4.addWidget(main.toolbar4)

        main.tableWidget_4.setColumnCount(6)
        main.tableWidget_4.setRowCount(count_row)
        main.tableWidget_4.setHorizontalHeaderLabels(["MethodRungeKuttaMersonX", "MethodRungeKuttaMersonY","MethodRungeKutta4X", "MethodRungeKutta4Y", "MethodGiraNewtonX", "MethodGiraNewtonY"])

        for i in range(count_row):
            main.tableWidget_4.setItem(i, 0 , QTableWidgetItem(str(MRK.arrayPointRungeX[i])) )
            main.tableWidget_4.setItem(i, 1 , QTableWidgetItem(str(MRK.arrayPointRungeY[i])) )
            main.tableWidget_4.setItem(i, 2 , QTableWidgetItem(str(MRK4.arrayPointRungeX[i])) )
            main.tableWidget_4.setItem(i, 3 , QTableWidgetItem(str(MRK4.arrayPointRungeY[i])) )
            main.tableWidget_4.setItem(i, 4 , QTableWidgetItem(str(x[i])) )
            main.tableWidget_4.setItem(i, 5 , QTableWidgetItem(str(y[i])) )

        main.tableWidget_4.resizeColumnsToContents()
    except ValueError :
        QMessageBox.about(main, "Warning", "Please enter a real number in the field!")
    except Exception:
        QMessageBox.about(main, "Warning", "Please check your entries. Something went wrong...")

def third_button(main):
    try:
        count_row = 1000
        MRK = MethodRungeKutta4ForUser3D()
        MGN = MethodGiraNMForUser3D()
        w = 0
        v = 0
        alfa = 0
        beta = 0
        if main.step3D.text() != "" :
            if is_digit(main.step3D.text()) :
                MRK.setStep(float(main.step3D.text()))
                MGN.setStep(float(main.step3D.text()))
            else:
                raise ValueError("Enter the number!")

        if main.StartX3D.text() != "" or main.StartY3D.text() != "" or main.StartZ3D.text() != "":
            if main.StartX3D.text() == "" or main.StartY3D.text() == "" or main.StartZ3D.text() == "" :
                raise Exception("Invalid input start values!")
            if is_digit(main.StartX3D.text()) and is_digit(main.StartY3D.text()) and is_digit(main.StartZ3D.text()):
                MRK.setStartPoint(float(main.StartX3D.text()), float(main.StartY3D.text()), float(main.StartZ3D.text()))
                MGN.setStartPoint(float(main.StartX3D.text()), float(main.StartY3D.text()), float(main.StartZ3D.text()))
            else:
                raise ValueError("Enter the number!")

        if main.StartIter3D.text() != "" :
            if main.StartIter3D.text().isdigit():
                count_row = int(main.StartIter3D.text())
                MRK.setIter(int(main.StartIter3D.text()))
                MGN.setIter(int(main.StartIter3D.text()))
            else:
                raise ValueError("Enter the number!")

        if main.helperW3D.text() != "" :
            if is_digit(main.helperW3D.text()):
                w = float(main.helperW3D.text())
            else:
                raise ValueError("Enter the number!")

        if main.helperV3D.text() != "" :
            if is_digit(main.helperV3D.text()):
                v = float(main.helperV3D.text())
            else:
                raise ValueError("Enter the number!")

        if main.helperAlfa3D.text() != "" :
            if is_digit(main.helperAlfa3D.text()):
                alfa = float(main.helperAlfa3D.text())
            else:
                raise ValueError("Enter the number!")

        if main.helperBeta3D.text() != "" :
            if is_digit(main.helperBeta3D.text()):
                beta = float(main.helperBeta3D.text())
            else:
                raise ValueError("Enter the number!")

        if main.system3D1.text() == "" or main.system3D2.text() == "" or main.system3D3.text() == "" :
            return  

        function1 = main.system3D1.text()
        function2 = main.system3D2.text()
        function3 = main.system3D3.text()

        MRK.startMethodRunge(function1, function2, function3, w, v, alfa, beta)
        x, y, z = MGN.startComputing(function1, function2, function3, w, v, alfa, beta)

        fig = plt.figure()
        ax = plt.axes( projection='3d' )
        ax.plot3D(MRK.arrayPointRungeX, MRK.arrayPointRungeY, MRK.arrayPointRungeZ, label='MethodRungeKutta', color = 'b')
        ax.plot3D(x, y, z, label = 'MethodGiraNewton', color = 'g')
        #ax.plot3D(MRK.arrayPointRungeX, MRK.arrayPointRungeY, MRK.arrayPointRungeZ)
        #ax.plot3D(x, y, z)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        ax.legend()
        plt.show()
        main.canavas3 = MyMplCanavas(fig)
        for i in reversed(range(main.componovka3.count())): 
            main.componovka3.itemAt(i).widget().deleteLater()
        main.componovka3.addWidget(main.canavas3)
        main.toolbar3 = NavigationToolbar(main.canavas3, main)
        main.componovka3.addWidget(main.toolbar3)

        main.tableWidget_2.setColumnCount(6)
        main.tableWidget_2.setRowCount(count_row)
        main.tableWidget_2.setHorizontalHeaderLabels(["MethodRungeKuttaX", "MethodRungeKuttaY", "MethodRungeKuttaZ", "MethodGiraNewtonX", "MethodGiraNewtonY", "MethodGiraNewtonZ"])

        for i in range(count_row):
            main.tableWidget_2.setItem(i, 0 , QTableWidgetItem(str(MRK.arrayPointRungeX[i])) )
            main.tableWidget_2.setItem(i, 1 , QTableWidgetItem(str(MRK.arrayPointRungeY[i])) )
            main.tableWidget_2.setItem(i, 2 , QTableWidgetItem(str(MRK.arrayPointRungeZ[i])) )
            main.tableWidget_2.setItem(i, 3 , QTableWidgetItem(str(x[i])) )
            main.tableWidget_2.setItem(i, 4 , QTableWidgetItem(str(y[i])) )
            main.tableWidget_2.setItem(i, 5 , QTableWidgetItem(str(z[i])) )

        main.tableWidget_2.resizeColumnsToContents()
    except ValueError :
        QMessageBox.about(main, "Warning", "Please enter a real number in the field!")
    except Exception:
        QMessageBox.about(main, "Warning", "Please check your entries. Something went wrong...")

def second_button(main):
    try:
        count_row = 1000
        MRK = MethodRungeKutta4ForUser()
        MGN = MethodGiraNMForUser()
        w = 0
        v = 0
        if main.step2D.text() != "" :
            if is_digit(main.step2D.text()) :
                MRK.setStep(float(main.step2D.text()))
                MGN.setStep(float(main.step2D.text()))
            else:
                raise ValueError("Enter the number!")

        if main.Start2DX.text() != "" or main.Start2DY.text() != "" :
            if main.Start2DX.text() == "" or main.Start2DY.text() == "" :
                raise Exception("Invalid input start values!")
            if is_digit(main.Start2DX.text()) and is_digit(main.Start2DY.text()):
                MRK.setStartPoint(float(main.Start2DX.text()), float(main.Start2DY.text()))
                MGN.setStartPoint(float(main.Start2DX.text()), float(main.Start2DY.text()))
            else:
                raise ValueError("Enter the number!")

        if main.StartIter2.text() != "" :
            if main.StartIter2.text().isdigit():
                count_row = int(main.StartIter2.text())
                MRK.setIter(int(main.StartIter2.text()))
                MGN.setIter(int(main.StartIter2.text()))
            else:
                raise ValueError("Enter the number!")

        if main.helperW2D.text() != "" :
            if is_digit(main.helperW2D.text()):
                w = float(main.helperW2D.text())
            else:
                raise ValueError("Enter the number!")

        if main.helperV2D.text() != "" :
            if is_digit(main.helperV2D.text()):
                v = float(main.helperV2D.text())
            else:
                raise ValueError("Enter the number!")

        if main.system2D1.text() == "" or main.system2D2.text() == "":
            return  

        function1 = main.system2D1.text()
        function2 = main.system2D2.text()

        MRK.startMethodRunge(function1, function2, w, v)
        x, y = MGN.startComputing(function1, function2, w, v)

        fig = Figure()
        axes = fig.add_subplot(111)
        axes.plot(MRK.arrayPointRungeX, MRK.arrayPointRungeY, label='MethodRungeKutta')
        axes.plot(x, y, label = 'MethodGiraNewton')
        axes.set_xlabel('x')
        axes.yaxis.set_label_position("right")
        axes.set_ylabel('     y', rotation = 0)
        axes.legend()
        main.canavas2 = MyMplCanavas(fig)
        for i in reversed(range(main.componovka2.count())): 
            main.componovka2.itemAt(i).widget().deleteLater()
        main.componovka2.addWidget(main.canavas2)
        main.toolbar2 = NavigationToolbar(main.canavas2, main)
        main.componovka2.addWidget(main.toolbar2)

        main.tableWidget.setColumnCount(4)
        main.tableWidget.setRowCount(count_row)
        main.tableWidget.setHorizontalHeaderLabels(["MethodRungeKuttaX", "MethodRungeKuttaY", "MethodGiraNewtonX", "MethodGiraNewtonY"])

        for i in range(count_row):
            main.tableWidget.setItem(i, 0 , QTableWidgetItem(str(MRK.arrayPointRungeX[i])) )
            main.tableWidget.setItem(i, 1 , QTableWidgetItem(str(MRK.arrayPointRungeY[i])) )
            main.tableWidget.setItem(i, 2 , QTableWidgetItem(str(x[i])) )
            main.tableWidget.setItem(i, 3 , QTableWidgetItem(str(y[i])) )

        main.tableWidget.resizeColumnsToContents()
    except ValueError :
        QMessageBox.about(main, "Warning", "Please enter a real number in the field!")
    except Exception:
        QMessageBox.about(main, "Warning", "Please check your entries. Something went wrong...")

def first_button(main):
    try:
        #Проверяем номер системы
        if (main.spinBox.text() == "1"):
            mysys = SystemODY()
        if (main.spinBox.text() == "2"):
            mysys = SystemODY1()
        if (main.spinBox.text() == "3"):
            mysys = SystemODY2()
        if (main.spinBox.text() == "4"):
            mysys = SystemODY3()
        if (main.spinBox.text() == "5"):
            mysys = SystemODY4()

        MRK = MethodRungeKutta4()
        MGN = MethodGiraNM()
        MGI = MethodGira()

        #Проверяем начальные данные 
        if main.step1.text() != "" :
            if is_digit(main.step1.text()) :
                MRK.setStep(float(main.step1.text()))
                MGN.setStep(float(main.step1.text()))
                MGI.setStep(float(main.step1.text()))
            else:
                raise ValueError("Enter the number!")

        count_row = 1000

        if main.StartIter1.text() != "" :
            if main.StartIter1.text().isdigit():
                count_row = int(main.StartIter1.text())
                MRK.setIter(int(main.StartIter1.text()))
                MGN.setIter(int(main.StartIter1.text()))
                MGI.setIter(int(main.StartIter1.text()))
            else:
                raise ValueError("Enter the number!")

        if main.startX1.text() != "" or main.startY1.text() != "" :
            if main.startX1.text() == "" or main.startY1.text() == "" :
                raise Exception("Invalid input start values!")
            if is_digit(main.startX1.text()) and is_digit(main.startY1.text()):
                MRK.setStartPoint(float(main.startX1.text()), float(main.startY1.text()))
                MGN.setStartPoint(float(main.startX1.text()), float(main.startY1.text()))
                MGI.setStartPoint(float(main.startX1.text()), float(main.startY1.text()))
            else:
                raise ValueError("Enter the number!")

        fig = Figure()
        axes = fig.add_subplot(111)
        MRK.startMethodRunge(mysys)
        MGI.Iteration(mysys)
        x, y = MGN.startComputing(mysys)
        axes.plot(MRK.arrayPointRungeX, MRK.arrayPointRungeY, label='MethodRungeKutta')
        axes.plot(x, y, label = 'MethodGiraNewton')
        axes.plot(MGI.arrayPointSIMX, MGI.arrayPointSIMY, label = 'MethonGiraSIM')
        axes.set_xlabel('x')
        axes.yaxis.set_label_position("right")
        axes.set_ylabel('     y', rotation=0)
        axes.legend()
        main.canavas = MyMplCanavas(fig)
        for i in reversed(range(main.componovka.count())): 
            main.componovka.itemAt(i).widget().deleteLater()
        main.componovka.addWidget(main.canavas)
        main.toolbar = NavigationToolbar(main.canavas, main)
        main.componovka.addWidget(main.toolbar)

        main.tableView1.setColumnCount(6)
        main.tableView1.setRowCount(count_row)
        main.tableView1.setHorizontalHeaderLabels(["MethodRungeKuttaX", "MethodRungeKuttaY", "MethodGiraNewtonX", "MethodGiraNewtonY", "MethodGiraSIMX", "MethodGiraSIMY"])

        for i in range(count_row):
            main.tableView1.setItem(i, 0 , QTableWidgetItem(str(MRK.arrayPointRungeX[i])) )
            main.tableView1.setItem(i, 1 , QTableWidgetItem(str(MRK.arrayPointRungeY[i])) )
            main.tableView1.setItem(i, 2 , QTableWidgetItem(str(x[i])) )
            main.tableView1.setItem(i, 3 , QTableWidgetItem(str(y[i])) )
            main.tableView1.setItem(i, 4 , QTableWidgetItem(str(MGI.arrayPointSIMX[i])) )
            main.tableView1.setItem(i, 5 , QTableWidgetItem(str(MGI.arrayPointSIMY[i])) )

        main.tableView1.resizeColumnsToContents()
    except ValueError :
        QMessageBox.about(main, "Warning", "Please enter a real number in the field!")
    except Exception:
        QMessageBox.about(main, "Warning", "Please check your entries. Something went wrong...")

def setNumberSystem(value, main):
    system = SystemODY()
    if(value == 1):
        system = SystemODY()
    if(value == 2):
        system = SystemODY1()
    if(value == 3):
        system = SystemODY2()
    if(value == 4):
        system = SystemODY3() 
    if(value == 5):
        system = SystemODY4()
    main.StrSys1.setText(system.GetFunction1())
    main.StrSys2.setText(system.GetFunction2())


class MyMplCanavas(FigureCanvasQTAgg):
    def __init__(self, fig, parent = None):
        self.fig = fig
        FigureCanvasQTAgg.__init__(self, self.fig)
        FigureCanvasQTAgg.updateGeometry(self)

def main():
    app = QApplication(sys.argv)
    main = MainWindow()
    main.componovka = QVBoxLayout(main.plot1)
    main.componovka2 = QVBoxLayout(main.plot2)
    main.componovka3 = QVBoxLayout(main.plot3)
    main.componovka4 = QVBoxLayout(main.plot4)
    main.componovka5 = QVBoxLayout(main.plot5)
    main.componovka6 = QVBoxLayout(main.widget)
    main.ButtStart1.clicked.connect(lambda checked, main = main : first_button(main))
    main.spinBox.valueChanged.connect( lambda value, main = main : setNumberSystem(value, main))
    main.ButtStart2.clicked.connect(lambda checked, main = main : second_button(main))
    main.ButtStart3.clicked.connect(lambda checked, main = main : third_button(main))
    main.ButtStart4.clicked.connect(lambda checked, main = main : fourth_button(main))
    main.ButtStart5.clicked.connect(lambda checked, main = main : fifth_button(main))
    main.ButtStart6.clicked.connect(lambda checked, main = main : sixth_button(main))
    system = SystemODY()
    main.StrSys1.setText(system.GetFunction1())
    main.StrSys2.setText(system.GetFunction2())
    main.show()
    sys.exit(app.exec_())

main()		

from PyQt5 import QtWidgets, QtCore
import subprocess
import sys
import re
import math
class App:

	def __init__(self):
		# get current brightness 
		process = subprocess.Popen(['light'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		self.slidervalue, stderr = process.communicate()
		self.slidervalue = str(self.slidervalue)
		self.slidervalue = self.slidervalue.replace("\\n'", '')
		self.slidervalue = self.slidervalue.replace("b'", '')
		print(str(self.slidervalue))
		self.slidervalue = int(float(self.slidervalue))+1
		self.root = QtWidgets.QApplication([])
		self.mainWidget = QtWidgets.QWidget()
		self.mainLayout = QtWidgets.QVBoxLayout()
		self.mainWidget.setLayout(self.mainLayout)
		self.slider = QtWidgets.QSlider()
		self.slider.setMinimum(2)
		self.slider.setMaximum(100)
		self.slider.setValue(self.slidervalue)
		self.slider.setOrientation(QtCore.Qt.Horizontal)
		self.slider.setStyleSheet(self.stylesheet())
		self.slider.valueChanged[int].connect(self.changeValue)
		self.mainWidget.setGeometry(100,100,500,100)
		self.text1 = QtWidgets.QLabel()
		self.slidervalue = str(self.slidervalue)
		self.text1.setText('percentage is at {}'.format(self.slidervalue))
		self.mainLayout.addWidget(self.text1,)
		self.mainLayout.addWidget(self.slider)
		self.mainWidget.show()
		self.root.exec_()
	#    .call(['light', '-S', str(x)])

	def changeValue(self, value):
		print(value)
		value = str(value)
		self.slidervalue = value
		self.text1.setText("percentage is at {}".format(self.slidervalue))
		subprocess.call(['light', '-S', value])

	def stylesheet(self):
  		return """
			QSlider::groove:horizontal {
				background: white;
				height: 40px;
			}

			QSlider::sub-page:horizontal {
				background: #ffd27f;
				height: 40px;
			}

			QSlider::add-page:horizontal {
				background: #fff;
				height: 40px;

			}

			QSlider::handle:horizontal {
				background: #bbf;
				border: 2px;
				width: 10px;
				margin-top: 0px;
				margin-bottom: 0px;
				border-radius: 0px;
			}
			QSlider{
				margin-top: 25px;
				margin-left: 40px;
				margin-right: 40px;
				height: 100px;
				width: 550px;
			}
			.QLabel{
				background-color: red;
				margin-left: 100px;
				margin-top: 100px;
				font-size: 4em;
			}
		"""
app = App()


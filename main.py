from PyQt5 import QtWidgets, QtCore
import subprocess
import sys


class App:

	def __init__(self):
		self.root = QtWidgets.QApplication([])
		self.mainWidget = QtWidgets.QWidget()
		self.mainLayout = QtWidgets.QVBoxLayout()
		self.mainWidget.setLayout(self.mainLayout)
		self.slider = QtWidgets.QSlider()
		self.slider.setOrientation(QtCore.Qt.Horizontal)
		self.slider.setStyleSheet(self.stylesheet())
		self.mainLayout.addWidget(self.slider)
		self.mainWidget.show()
		self.root.exec_()
		process = subprocess.Popen(['light'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		self.slidervalue, stderr = process.communicate()
	#    .call(['light', '-S', str(x)])

	def stylesheet(self):
  		return """
			QSlider::groove:horizontal {
				background: white;
				height: 100px;
			}

			QSlider::sub-page:horizontal {
				background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,
					stop: 0 #66e, stop: 1 #bbf);
				background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,
					stop: 0 #bbf, stop: 1 #55f);
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
				margin-left: 25px;
				height: 200px;
				width: 500px;
			}
		"""
app = App()


from tkinter import *
import subprocess



class App:

	def __init__(self):
		self.root = Tk()
		self.root.title('Light')
		self.root.geometry('500x200')
		self.slidervalue = subprocess.call(['light'])

		process = subprocess.Popen(['light'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		self.slidervalue, stderr = process.communicate()

		self.slider = Scale(self.root, from_=2, to=100, 
							   orient="horizontal",)
		self.slider.set(self.slidervalue)
		print(self.slidervalue)
		self.slider.bind("<ButtonRelease-1>", self.updateValue)
		self.slider.pack()
		self.root.mainloop()
	def updateValue(self, event):
		self._job = self.root.after(500, self._do_something)

	def _do_something(self):
		self._job = None
		print( "new value:", self.slider.get())
		x = self.slider.get()
		subprocess.call(['light', '-S', str(x)])

app = App()


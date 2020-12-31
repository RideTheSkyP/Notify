from kivy.properties import BooleanProperty
from kivymd.uix.screen import MDScreen


class level5(MDScreen):
	first = BooleanProperty(False)
	second = BooleanProperty(False)
	third = BooleanProperty(False)
	fourth = BooleanProperty(False)
	fifth = BooleanProperty(False)
	buttonOpacity = BooleanProperty(False)

	def __init__(self, **kw):
		super().__init__(**kw)

	def changeState(self, num):
		if num == 0:
			num = 1
		else:
			num = 0
		return num

	def thirdPressed(self):
		self.first = self.changeState(self.first)
		self.third = self.changeState(self.third)
		self.fourth = self.changeState(self.fourth)
		self.checkTruth()

	def secondPressed(self):
		self.first = self.changeState(self.first)
		self.second = self.changeState(self.second)
		self.fourth = self.changeState(self.fourth)
		self.checkTruth()

	def firstPressed(self):
		self.second = self.changeState(self.second)
		self.third = self.changeState(self.third)
		self.fifth = self.changeState(self.fifth)
		self.checkTruth()

	def checkTruth(self):
		if self.first == 1 and self.second == 0 and self.third == 1 and self.fourth == 1 and self.fifth == 1:
			self.buttonOpacity = 1

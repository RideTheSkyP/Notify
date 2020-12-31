from kivy.properties import BooleanProperty
from kivymd.uix.screen import MDScreen


class easter(MDScreen):
	textField = BooleanProperty(False)
	showCodeField = BooleanProperty(False)
	first = BooleanProperty(False)
	second = BooleanProperty(False)
	last = BooleanProperty(False)

	def __init__(self, **kw):
		super().__init__(**kw)

	def hideTextField(self):
		self.textField = True

	def hideButtons(self):
		self.first, self.second, self.last, self.showCodeField = 0, 0, 0, 1

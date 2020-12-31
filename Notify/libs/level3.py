from kivy.properties import BooleanProperty
from kivymd.uix.screen import MDScreen


class level3(MDScreen):
	first = BooleanProperty(False)
	second = BooleanProperty(False)
	third = BooleanProperty(False)
	fourth = BooleanProperty(False)
	fifth = BooleanProperty(False)
	sixth = BooleanProperty(False)
	seventh = BooleanProperty(False)
	last = BooleanProperty(False)

	def __init__(self, **kw):
		super().__init__(**kw)

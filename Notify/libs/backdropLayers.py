from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.backdrop import MDBackdrop, MDBackdropFrontLayer, MDBackdropBackLayer
from kivy.uix.recycleview import RecycleView
from kivymd.uix.floatlayout import FloatLayout


class NotifyBackdropLayer(MDBackdrop):
	pass


class NotifyBackdropFrontLayer(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		print(self)
		# self.createHomeScreen()

	def createHomeScreen(self):
		self.add_widget(MDLabel(text="Home"))


class NotifyBackdropBackLayerSettings(FloatLayout):
	pass

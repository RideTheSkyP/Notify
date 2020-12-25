from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.animation import Animation
from kivymd.uix.label import MDLabel
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.backdrop import MDBackdrop, MDBackdropFrontLayer, MDBackdropBackLayer
from kivy.uix.recycleview import RecycleView
from kivymd.uix.floatlayout import FloatLayout


class NotifyBackdropLayer(MDBackdrop):
	def closing_animation_backdrop_components_settings(self, instance_backdrop, instance_backlayer):
		Animation(scale_x=0, scale_y=0, d=0.2).start(instance_backlayer)
		anim = Animation(opacity=0, d=0.2)
		anim.bind(on_complete=self.set_instance_backdrop_title_settings)
		anim.start(instance_backdrop.ids.toolbar.ids.label_title)

	def opening_animation_backdrop_components_settings(self, instance_backdrop, instance_backlayer):
		Animation(scale_x=1, scale_y=1, d=0.2).start(instance_backlayer)
		anim = Animation(opacity=0, d=0.2)
		anim.bind(on_complete=self.set_instance_backdrop_title_settings)
		anim.start(instance_backdrop.ids.toolbar.ids.label_title)

	def set_instance_backdrop_title_settings(self, instance_animation, instance_backdrop):
		instance_backdrop.text = ("Notify" if instance_backdrop.text == "Themes" else "Themes")
		Animation(opacity=1, d=0.2).start(instance_backdrop)


class NotifyBackdropFrontLayer(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		print(self)
		# self.createHomeScreen()

	def createHomeScreen(self):
		self.add_widget(MDLabel(text="Home"))


class NotifyBackdropBackLayerSettings(FloatLayout):
	pass

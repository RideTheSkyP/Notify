from kivy.animation import Animation
from kivymd.uix.backdrop import MDBackdrop
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.screen import MDScreen
from Not.calend import MDDatePicker
from kivymd.uix.button import MDFloatingActionButtonSpeedDial


# from kivymd.uix import picker1


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


class NotifyBackdropFrontLayer(MDScreen):
    data = {"tree-outline": "Go for a walk",
            "tennis": "Sport",
            "tea-outline": "Make a break",
            "briefcase-outline": "Work",
            "bookshelf": "Chill"}

    def __init__(self, **kw):
        super().__init__(**kw)
        self.createCalendar()

    def createCalendar(self):
        self.add_widget(MDDatePicker(callback=self.getSelectedDate))

    def getSelectedDate(self, date):
        print(date)

    def getActionButton(self, instance):
        print(instance.icon)
        print(self.ids.screen.ids)


class NotifyBackdropBackLayerSettings(FloatLayout):
    pass

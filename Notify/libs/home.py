from kivy.animation import Animation
from kivy.uix.screenmanager import Screen
from kivymd.uix.screen import MDScreen
from kivymd.uix.picker import MDDatePicker


class Home(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        # print(self)
    #     self.createCalendar()
    #
    # def createCalendar(self):
    #     self.add_widget(MDDatePicker(callback=self.getSelectedDate, size=(self.width, self.height)))
    #
    # def getSelectedDate(self, date):
    #     print(date)

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

    def closing_animation_backdrop_components_menu(self, instance_backdrop, instance_backlayer):
        Animation(scale_x=0, scale_y=0, d=0.2).start(instance_backlayer)
        anim = Animation(opacity=0, d=0.2)
        anim.bind(on_complete=self.set_instance_backdrop_title_menu)
        anim.start(instance_backdrop.ids.toolbar.ids.label_title)

    def opening_animation_backdrop_components_menu(self, instance_backdrop, instance_backlayer):
        Animation(scale_x=1, scale_y=1, d=0.2).start(instance_backlayer)
        anim = Animation(opacity=0, d=0.2)
        anim.bind(on_complete=self.set_instance_backdrop_title_menu)
        anim.start(instance_backdrop.ids.toolbar.ids.label_title)

    def set_instance_backdrop_title_menu(self, instance_animation, instance_backdrop):
        instance_backdrop.text = ("Notify" if instance_backdrop.text == "Themes" else "Themes")
        Animation(opacity=1, d=0.2).start(instance_backdrop)


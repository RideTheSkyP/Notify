import ast
import os
import sys
from pathlib import Path
from kivy.core.window import Window
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.loader import Loader
from kivy.properties import ObjectProperty
from libs.dialog_change_theme import NotifyDialogChangeTheme
from kivymd.uix.selectioncontrol import MDCheckbox, MDSwitch, MDIcon
from libs.list_items import NotifyOneLineLeftIconItem, NotifyOneLineIconListItem
from kivymd.uix.backdrop import MDBackdrop
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivymd.uix.backdrop import MDBackdropFrontLayer
from kivymd import images_path
from kivymd.app import MDApp
# from kivymd.uix.picker import MDDatePicker, MDTimePicker
# from test import MDDatePicker
from libs.navigationDrawer import ItemDrawer, DrawerList
from kivymd.stiffscroll import StiffScrollEffect
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton
from kivymd.uix.toolbar import MDBottomAppBar
from kivymd.uix.bottomnavigation import MDBottomNavigation
from kivymd.uix.boxlayout import BoxLayout
from kivy.core.window import Window
import calendar


os.environ["KIVY_PROFILE_LANG"] = "1"

if getattr(sys, "frozen", False):  # bundle mode with PyInstaller
    os.environ["NOTIFY_ROOT"] = sys._MEIPASS
else:
    sys.path.append(os.path.abspath(__file__).split("demos")[0])
    os.environ["NOTIFY_ROOT"] = str(Path(__file__).parent)
    # os.environ["NOTIFY_ROOT"] = os.path.dirname(os.path.abspath(__file__))

os.environ["NOTIFY_ASSETS"] = os.path.join(os.environ["NOTIFY_ROOT"], f"assets{os.sep}")
Window.softinput_mode = "below_target"


class NotifyApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette = "Teal"
        self.dialog_change_theme = None
        self.toolbar = None
        self.data_screens = {}
        Loader.loading_image = f"{images_path}transparent.png"

    def build(self):
        Builder.load_file(f"{os.environ['NOTIFY_ROOT']}/libs/kv/list_items.kv")
        # MDDatePicker(callback=self.getSelectedDate)
        return Builder.load_file(f"{os.environ['NOTIFY_ROOT']}/libs/kv/start_screen.kv")

    def show_dialog_change_theme(self):
        if not self.dialog_change_theme:
            self.dialog_change_theme = NotifyDialogChangeTheme()
            self.dialog_change_theme.set_list_colors_themes()
        self.dialog_change_theme.open()

    def on_start(self):
        # self.fps_monitor_start()
        Builder.load_file(f"{os.environ['NOTIFY_ROOT']}/libs/kv/dialog_change_theme.kv", )
        # self.root.ids.home.height = self.root.ids.home.height - self.root.ids.bottomNavigation.height
        print(self.root)
        # self.root.ids.home.add_widget(MDDatePicker(callback=self.getSelectedDate))

        with open(f"{os.environ['NOTIFY_ROOT']}/screens_data.json") as read_file:
            self.data_screens = ast.literal_eval(read_file.read())
            data_screens = list(self.data_screens.keys())
            data_screens.sort()
        for name_item_example in data_screens:
            self.root.ids.contentDrawer.ids.drawerList.add_widget(ItemDrawer(
                text=name_item_example,
                icon=self.data_screens[name_item_example]["icon"],
                # on_release=self.set_example_screen(name_item_example)
            ))

    def set_example_screen(self, name_screen):
        manager = self.root.ids.screen_manager

        if not manager.has_screen(self.data_screens[name_screen]["name_screen"]):
            name_kv_file = self.data_screens[name_screen]["kv_string"]
            Builder.load_file(f"{os.environ['NOTIFY_ROOT']}/libs/kv/{name_kv_file}.kv", )
            if "Import" in self.data_screens[name_screen]:
                exec(self.data_screens[name_screen]["Import"])
            screen_object = eval(self.data_screens[name_screen]["Factory"])
            self.data_screens[name_screen]["object"] = screen_object
            if "toolbar" in screen_object.ids:
                screen_object.ids.toolbar.title = name_screen
            manager.add_widget(screen_object)
        manager.current = self.data_screens[name_screen]["name_screen"]

    def back_to_home_screen(self):
        self.root.ids.screen_manager.current = "home"

    def switch_theme_style(self, state):
        self.theme_cls.theme_style = "Dark" if state else "Light"
        # self.theme_cls.text_color = "Gray" if state else "Light"

    # def show_time_picker(self):
    #     time_dialog = MDTimePicker()
    #     time_dialog.open()

    def getSelectedDate(self, date):
        print(date)
    #
    # def datePicker(self):
    #     calendarWidget = MDDatePicker(callback=self.getSelectedDate)
    #     calendarWidget.open()


NotifyApp().run()

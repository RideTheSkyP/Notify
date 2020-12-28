import ast
import os
import sys
from pathlib import Path
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.loader import Loader
from kivy.properties import ObjectProperty, StringProperty
from libs.dialog_change_theme import NotifyDialogChangeTheme
from libs.listItems import NotifyOneLineLeftIconItem, NotifyOneLineIconListItem, ItemDrawer
from kivymd import images_path
from kivymd.app import MDApp
from kivy.core.window import Window
from libs.navigationDrawer import DrawerList
from kivymd.stiffscroll import StiffScrollEffect
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton
from kivymd.uix.toolbar import MDBottomAppBar
from kivymd.uix.bottomnavigation import MDBottomNavigation
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.backdrop import MDBackdrop
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivymd.uix.backdrop import MDBackdropFrontLayer
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.picker import MDDatePicker, MDTimePicker
from kivymd.uix.selectioncontrol import MDCheckbox, MDSwitch, MDIcon
from kivymd.uix.banner import MDBanner


os.environ["KIVY_PROFILE_LANG"] = "1"

if getattr(sys, "frozen", False):  # bundle mode with PyInstaller
    os.environ["NOTIFY_ROOT"] = sys._MEIPASS
else:
    sys.path.append(os.path.abspath(__file__).split("Project")[0])
    os.environ["NOTIFY_ROOT"] = str(Path(__file__).parent)

os.environ["NOTIFY_ASSETS"] = os.path.join(os.environ["NOTIFY_ROOT"], f"assets{os.sep}")
Window.softinput_mode = "below_target"


class NotifyApp(MDApp):

    hintText = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette = "Teal"
        self.dialog_change_theme = None
        self.toolbar = None
        # self.hintText = ""
        self.screensData = {}
        Loader.loading_image = f"{images_path}transparent.png"

    def build(self):
        Builder.load_file(f"{os.environ['NOTIFY_ROOT']}/libs/kv/listItems.kv")
        Builder.load_file(f"{os.environ['NOTIFY_ROOT']}/libs/kv/backdropLayers.kv")
        Builder.load_file(f"{os.environ['NOTIFY_ROOT']}/libs/kv/navigationDrawer.kv")
        Builder.load_file(f"{os.environ['NOTIFY_ROOT']}/libs/kv/dialog_change_theme.kv")
        Builder.load_file(f"{os.environ['NOTIFY_ROOT']}/libs/kv/toolbar.kv")
        return Builder.load_file(f"{os.environ['NOTIFY_ROOT']}/libs/kv/startScreen.kv")

    def show_dialog_change_theme(self):
        if not self.dialog_change_theme:
            self.dialog_change_theme = NotifyDialogChangeTheme()
            self.dialog_change_theme.set_list_colors_themes()
        self.dialog_change_theme.open()

    def on_start(self):
        # self.fps_monitor_start()
        print(f"{self.root.ids.backdropLayers.ids.frontLayerItems}")
        # self.root.ids.home.add_widget(MDDatePicker(callback=self.getSelectedDate))

        with open(f"{os.environ['NOTIFY_ROOT']}/screens_data.json") as read_file:
            self.screensData = ast.literal_eval(read_file.read())
            screensData = list(self.screensData.keys())
            screensData.sort()

        for name_item_example in screensData:
            self.root.ids.contentDrawer.ids.drawerList.add_widget(ItemDrawer(
                text=name_item_example,
                icon=self.screensData[name_item_example]["icon"],
            ))
            self.set_example_screen(name_item_example)

    def set_example_screen(self, screenName):
        manager = self.root.ids.screenManager

        if not manager.has_screen(self.screensData[screenName]["screenName"]):
            Builder.load_file(f"{os.environ['NOTIFY_ROOT']}/libs/kv/{self.screensData[screenName]['screenName']}.kv",)
            if "Import" in self.screensData[screenName]:
                exec(self.screensData[screenName]["Import"])
            screen_object = eval(self.screensData[screenName]["Factory"])
            self.screensData[screenName]["object"] = screen_object
            if "toolbar" in screen_object.ids:
                screen_object.ids.toolbar.title = screenName
            manager.add_widget(screen_object)
            print(f"Builder: {Builder.files}\nFactory: {Factory.classes}\nManager: {manager.screens}")

    def openScreen(self, screenName):
        self.root.ids.screenManager.current = self.screensData[screenName]["screenName"]

    def backToHomeScreen(self):
        self.root.ids.screenManager.current = "home"

    def switch_theme_style(self, state):
        self.theme_cls.theme_style = "Dark" if state else "Light"
        # self.theme_cls.text_color = "Gray" if state else "Light"

    def showHint(self, screenName):
        for key, value in self.screensData.items():
            if screenName in value.get("screenName"):
                self.hintText = self.screensData[key]["hint"]

    def getSelectedDate(self, date):
        if str(date) == self.screensData["Home"]["answer"]:
            print(str(date))

    def datePicker(self):
        calendarWidget = MDDatePicker(callback=self.getSelectedDate)
        calendarWidget.open()


NotifyApp().run()

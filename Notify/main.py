import ast
import os
import sys
from pathlib import Path
from kivy.core.window import Window
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.loader import Loader
from libs.dialog_change_theme import NotifyDialogChangeTheme
# from kivymd.uix.selectioncontrol import
from libs.list_items import NotifyOneLineLeftIconItem, NotifyOneLineIconListItem
from kivymd.uix.backdrop import MDBackdrop
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivymd.uix.backdrop import MDBackdropFrontLayer

from kivymd import images_path
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton
from kivymd.uix.toolbar import MDBottomAppBar
from kivymd.uix.bottomnavigation import MDBottomNavigation
from kivymd.uix.boxlayout import BoxLayout

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
        return Builder.load_file(f"{os.environ['NOTIFY_ROOT']}/libs/kv/start_screen.kv")

    def show_dialog_change_theme(self):
        if not self.dialog_change_theme:
            self.dialog_change_theme = NotifyDialogChangeTheme()
            self.dialog_change_theme.set_list_colors_themes()
        self.dialog_change_theme.open()

    def on_start(self):
        self.fps_monitor_start()
        Builder.load_file(f"{os.environ['NOTIFY_ROOT']}/libs/kv/dialog_change_theme.kv",)
        print(self.root.ids.contentDrawer.ids)

        with open(f"{os.environ['NOTIFY_ROOT']}/screens_data.json") as read_file:
            self.data_screens = ast.literal_eval(read_file.read())
            data_screens = list(self.data_screens.keys())
            data_screens.sort()
        for name_item_example in data_screens:
            self.root.ids.contentDrawer.ids.drawerList.add_widget(NotifyOneLineIconListItem(
                text=name_item_example,
                icon=self.data_screens[name_item_example]["icon"],
                # on_release=self.set_example_screen(name_item_example)
            ))

    def set_example_screen(self, name_screen):
        manager = self.root.ids.screen_manager

        if not manager.has_screen(self.data_screens[name_screen]["name_screen"]):
            name_kv_file = self.data_screens[name_screen]["kv_string"]
            Builder.load_file(f"{os.environ['NOTIFY_ROOT']}/libs/kv/{name_kv_file}.kv",)
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


NotifyApp().run()

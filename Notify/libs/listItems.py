from kivy.properties import ListProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import RectangularElevationBehavior
from kivymd.uix.list import ILeftBody, IRightBodyTouch, OneLineAvatarListItem, OneLineIconListItem, \
    TwoLineAvatarListItem
from kivymd.uix.selectioncontrol import MDCheckbox, MDSwitch


class NotifyOneLineLeftAvatarItem(OneLineAvatarListItem):
    divider = None
    source = StringProperty()


class NotifyTwoLineLeftAvatarItem(TwoLineAvatarListItem):
    icon = StringProperty()
    secondary_font_style = "Caption"


class NotifyTwoLineLeftIconItem(TwoLineAvatarListItem):
    icon = StringProperty()


class NotifyOneLineLeftIconItem(OneLineAvatarListItem):
    icon = StringProperty()


class NotifyOneLineIconListItem(OneLineIconListItem):
    icon = StringProperty()


class NotifyOneLineLeftWidgetItem(OneLineAvatarListItem):
    color = ListProperty()


class LeftWidget(ILeftBody, Widget):
    pass


class IconRightSampleWidget(IRightBodyTouch, MDCheckbox):
    pass


class ContentNavigationDrawer(BoxLayout):
    pass


class NotifyThemeStyleSwitch(MDSwitch):
    pass


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))


class NotifyFloatingLabel(ThemableBehavior, RectangularElevationBehavior, BoxLayout):
    text = StringProperty()
    text_color = ListProperty()
    bg_color = ListProperty()

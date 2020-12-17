from kivy.properties import ListProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivymd.uix.list import ILeftBody, IRightBodyTouch, OneLineAvatarListItem, OneLineIconListItem, \
    TwoLineAvatarListItem, IconLeftWidget
from kivymd.uix.selectioncontrol import MDCheckbox


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

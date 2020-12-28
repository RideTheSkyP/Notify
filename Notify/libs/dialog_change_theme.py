from kivy.uix.modalview import ModalView
from kivy.utils import get_color_from_hex
from kivymd.color_definitions import colors, palette
from kivymd.theming import ThemableBehavior


class NotifyBaseDialog(ThemableBehavior, ModalView):
    pass


class NotifyDialogDev(NotifyBaseDialog):
    pass


class NotifyDialogChangeTheme(NotifyBaseDialog):
    def set_list_colors_themes(self):
        for name_theme in palette:
            self.ids.rv.data.append(
                {
                    "viewclass": "NotifyOneLineLeftWidgetItem",
                    "color": get_color_from_hex(colors[name_theme]["500"]),
                    "text": name_theme,
                }
            )

__all__ = ("MDDatePicker",)

import calendar
import datetime
from datetime import date

from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import (
    BooleanProperty,
    ListProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
)
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.modalview import ModalView
from kivy.utils import get_color_from_hex
from kivymd.color_definitions import colors, palette
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import (
    CircularRippleBehavior,
    RectangularElevationBehavior,
    SpecificBackgroundColorBehavior,
)
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel


Builder.load_string("""
#:import calendar calendar


<MDDatePicker>
    background: "{}/transparent.png".format(images_path)
    cal_layout: cal_layout
    size_hint: (None, None)
    size:
        (dp(328), dp(484)) \
        if self.theme_cls.device_orientation == "portrait" \
        else (dp(512), dp(304))
    pos_hint: {"center_x": .5, "center_y": .5}
    
    MDLabel:
        id: label_full_date
        font_style: "H4"
        # text_color: root.specific_text_color
        theme_text_color: "Custom"
        size_hint: (None, None)
        size:
            (root.width, dp(30)) \
            if root.theme_cls.device_orientation == "portrait" \
            else (dp(168), dp(30))
        pos:
            (root.pos[0] + dp(23), root.pos[1] + root.height - dp(300)) \
            if root.theme_cls.device_orientation == "portrait" \
            else (root.pos[0] + dp(3), root.pos[1] + dp(214))
        line_height: .84
        valign: "middle"
        text_size:
            (root.width, None) \
            if root.theme_cls.device_orientation == "portrait" \
            else (dp(149), None)
        bold: True
        text:
            root.fmt_lbl_date(root.sel_year, root.sel_month, root.sel_day, root.theme_cls.device_orientation)

    # MDLabel:
    #     id: label_year
    #     font_style: "Subtitle1"
    #     text_color: root.specific_text_color
    #     theme_text_color: "Custom"
    #     size_hint: (None, None)
    #     size: root.width, dp(30)
    #     pos:
    #         (root.pos[0] + dp(23), root.pos[1] + root.height - dp(40)) \
    #         if root.theme_cls.device_orientation == "portrait" \
    #         else (root.pos[0] + dp(16), root.pos[1] + root.height - dp(41))
    #     valign: "middle"
    #     text: str(root.sel_year)

    MDGridLayout:
        id: cal_layout
        cols: 7
        # adaptive_size: True
        size:
            (dp(44 * 7), dp(40 * 7)) \
            if root.theme_cls.device_orientation == "portrait" else (dp(46 * 7), dp(32 * 7))
        col_default_width:
            dp(42) if root.theme_cls.device_orientation == "portrait" else dp(39)
        size_hint: (None, None)
        padding:
            (dp(2), 0) if root.theme_cls.device_orientation == "portrait" else (dp(7), 0)
        spacing:
            (dp(2), 0) if root.theme_cls.device_orientation == "portrait" else (dp(7), 0)
        pos:
            (root.pos[0] + dp(10), root.pos[1] + dp(160)) \
            if root.theme_cls.device_orientation == "portrait" else (root.pos[0] + dp(168) + dp(8), root.pos[1] + dp(48))

    MDLabel:
        id: label_month_selector
        font_style: "Body2"
        text: calendar.month_name[root.month].capitalize() + " " + str(root.year)
        size_hint: (None, None)
        size: root.width, dp(30)
        pos: root.pos
        pos_hint:
            {"center_x": .5, "center_y": .95} \
            if self.theme_cls.device_orientation == "portrait" \
            else {"center_x": .5, "center_y": .915}
        valign: "middle"
        halign: "center"

    MDIconButton:
        icon: "chevron-left"
        theme_text_color: "Secondary"
        pos_hint:
            {"center_x": .08, "center_y": .95} \
            if root.theme_cls.device_orientation == "portrait" else {"center_x": .39, "center_y": .95}
        on_release: root.change_month("prev")

    MDIconButton:
        icon: "chevron-right"
        theme_text_color: "Secondary"
        pos_hint:
            {"center_x": .92, "center_y": .95} \
            if root.theme_cls.device_orientation == "portrait" else {"center_x": .94, "center_y": .95}
        on_release: root.change_month("next")


<DayButton>
    size_hint: None, None
    size:
        (dp(40), dp(40)) if root.theme_cls.device_orientation == "portrait" else (dp(32), dp(32))

    MDLabel:
        font_style: "Caption"
        theme_text_color: "Custom" if root.is_today and not root.is_selected else "Primary"
        text_color: root.theme_cls.primary_color
        opposite_colors:
            root.is_selected if root.owner.sel_month == root.owner.month \
            and root.owner.sel_year == root.owner.year and str(self.text) == str(root.owner.sel_day) else False
        size_hint_x: None
        valign: "middle"
        halign: "center"
        text: root.text


<WeekdayLabel>
    font_style: "Caption"
    theme_text_color: "Secondary"
    size: (dp(40), dp(40)) if root.theme_cls.device_orientation == "portrait" else (dp(32), dp(32))
    size_hint: None, None
    text_size: self.size
    valign:
        "middle" if root.theme_cls.device_orientation == "portrait" else "bottom"
    halign: "center"


<DaySelector>
    size:
        (dp(40), dp(40)) if root.theme_cls.device_orientation == "portrait" \
        else (dp(32), dp(32))
    size_hint: (None, None)

    canvas:
        Color:
            rgba: self.theme_cls.primary_color if self.shown else [0, 0, 0, 0]
        Ellipse:
            size:
                (dp(40), dp(40)) if root.theme_cls.device_orientation == "portrait" else (dp(32), dp(32))
            pos:
                self.pos if root.theme_cls.device_orientation == "portrait" else (self.pos[0], self.pos[1])
""")


class DaySelector(ThemableBehavior, AnchorLayout):
    shown = BooleanProperty(False)

    def __init__(self, parent):
        super().__init__()
        self.parent_class = parent
        self.parent_class.add_widget(self, index=7)
        self.selected_widget = None
        Window.bind(on_resize=self.move_resize)

    def update(self):
        parent = self.parent_class
        if parent.sel_month == parent.month and parent.sel_year == parent.year:
            self.shown = True
        else:
            self.shown = False

    def set_widget(self, widget):
        self.selected_widget = widget
        self.pos = widget.pos
        self.move_resize(do_again=True)
        self.update()

    def move_resize(self, window=None, width=None, height=None, do_again=True):
        self.pos = self.selected_widget.pos
        if do_again:
            Clock.schedule_once(
                lambda x: self.move_resize(do_again=False), 0.01
            )


class DayButton(ThemableBehavior, CircularRippleBehavior, ButtonBehavior, AnchorLayout):
    text = StringProperty()
    owner = ObjectProperty()
    is_today = BooleanProperty(False)
    is_selected = BooleanProperty(False)

    def on_release(self):
        self.owner.set_selected_widget(self)


class WeekdayLabel(MDLabel):
    pass


class MDDatePicker(
    FloatLayout,
    ThemableBehavior,
    RectangularElevationBehavior,
    SpecificBackgroundColorBehavior,
):
    _sel_day_widget = ObjectProperty()
    cal_list = None
    cal_layout = ObjectProperty()
    sel_year = NumericProperty()
    sel_month = NumericProperty()
    sel_day = NumericProperty()
    day = NumericProperty()
    month = NumericProperty()
    year = NumericProperty()
    today = date.today()
    callback = ObjectProperty()
    background_color = ListProperty([0, 0, 0, 0.7])

    class SetDateError(Exception):
        pass

    def __init__(
        self,
        callback,
        year=None,
        month=None,
        day=None,
        firstweekday=0,
        min_date=None,
        max_date=None,
        **kwargs,
    ):
        self.callback = callback
        self.cal = calendar.Calendar(firstweekday)
        self.sel_year = year if year else self.today.year
        self.sel_month = month if month else self.today.month
        self.sel_day = day if day else self.today.day
        self.month = self.sel_month
        self.year = self.sel_year
        self.day = self.sel_day
        self.min_date = min_date
        self.max_date = max_date
        super().__init__(**kwargs)
        self.selector = DaySelector(parent=self)
        self.generate_cal_widgets()
        self.update_cal_matrix(self.sel_year, self.sel_month)
        self.set_month_day(self.sel_day)
        self.selector.update()

    def fmt_lbl_date(self, year, month, day, orientation):
        d = datetime.date(int(year), int(month), int(day))
        separator = "\n" if orientation == "landscape" else " "

        return (
            d.strftime("%a,").capitalize()
            + separator
            + d.strftime("%b").capitalize()
            + " "
            + str(day).lstrip("0")
        )

    def set_date(self, year, month, day):
        try:
            date(year, month, day)
        except Exception as e:
            if str(e) == "day is out of range for month":
                raise self.SetDateError(
                    " Day %s day is out of range for month %s" % (day, month)
                )
            elif str(e) == "month must be in 1..12":
                raise self.SetDateError(
                    "Month must be between 1 and 12, got %s" % month
                )
            elif str(e) == "year is out of range":
                raise self.SetDateError(
                    "Year must be between %s and %s, got %s"
                    % (datetime.MINYEAR, datetime.MAXYEAR, year)
                )
        else:
            self.sel_year = year
            self.sel_month = month
            self.sel_day = day
            self.month = self.sel_month
            self.year = self.sel_year
            self.day = self.sel_day
            self.update_cal_matrix(self.sel_year, self.sel_month)
            self.set_month_day(self.sel_day)
            self.selector.update()

    def set_selected_widget(self, widget):
        if self._sel_day_widget:
            self._sel_day_widget.is_selected = False
        widget.is_selected = True
        self.sel_month = int(self.month)
        self.sel_year = int(self.year)
        self.sel_day = int(widget.text)
        self._sel_day_widget = widget
        self.selector.set_widget(widget)
        self.callback(date(self.sel_year, self.sel_month, self.sel_day))

    def set_month_day(self, day):
        for idx in range(len(self.cal_list)):
            if str(day) == str(self.cal_list[idx].text):
                self._sel_day_widget = self.cal_list[idx]
                self.sel_day = int(self.cal_list[idx].text)
                if self._sel_day_widget:
                    self._sel_day_widget.is_selected = False
                self._sel_day_widget = self.cal_list[idx]
                self.cal_list[idx].is_selected = True
                self.selector.set_widget(self.cal_list[idx])

    def update_cal_matrix(self, year, month):
        try:
            dates = [x for x in self.cal.itermonthdates(year, month)]
        except ValueError as e:
            if str(e) == "year is out of range":
                pass
        else:
            self.year = year
            self.month = month
            for idx in range(len(self.cal_list)):
                if idx >= len(dates) or dates[idx].month != month:
                    self.cal_list[idx].disabled = True
                    self.cal_list[idx].text = ""
                else:
                    if self.min_date and self.max_date:
                        self.cal_list[idx].disabled = (
                            True
                            if (
                                dates[idx] < self.min_date
                                or dates[idx] > self.max_date
                            )
                            else False
                        )
                    elif self.min_date:
                        if isinstance(self.min_date, date):
                            self.cal_list[idx].disabled = (
                                True if dates[idx] < self.min_date else False
                            )
                        else:
                            raise ValueError(
                                "min_date must be of type {} or None, got {}".format(
                                    date, type(self.min_date)
                                )
                            )
                    elif self.max_date:
                        if isinstance(self.max_date, date):
                            self.cal_list[idx].disabled = (
                                True if dates[idx] > self.max_date else False
                            )
                        else:
                            raise ValueError(
                                "max_date must be of type {} or None, got {}".format(
                                    date, type(self.min_date)
                                )
                            )
                    else:
                        self.cal_list[idx].disabled = False
                    self.cal_list[idx].text = str(dates[idx].day)
                    self.cal_list[idx].is_today = dates[idx] == self.today
            self.selector.update()

    def generate_cal_widgets(self):
        cal_list = []
        for day in self.cal.iterweekdays():
            self.cal_layout.add_widget(
                WeekdayLabel(text=calendar.day_abbr[day][0].upper())
            )
        for i in range(6 * 7):  # 6 weeks, 7 days a week
            db = DayButton(owner=self)
            cal_list.append(db)
            self.cal_layout.add_widget(db)
        self.cal_list = cal_list

    def change_month(self, operation):
        op = 1 if operation == "next" else -1
        sl, sy = self.month, self.year
        m = 12 if sl + op == 0 else 1 if sl + op == 13 else sl + op
        y = sy - 1 if sl + op == 0 else sy + 1 if sl + op == 13 else sy
        self.update_cal_matrix(y, m)

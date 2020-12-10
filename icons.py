from kivymd.icon_definitions import md_icons
from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
<TooltipMDIconButton@MDIconButton+MDTooltip>
Screen:
	ScrollView:
		GridLayout:
			id: grid
			cols: 16
			size_hint_y: None
			height: self.minimum_height
			width: self.minimum_width
'''


class app(MDApp):
	def build(self):
		return Builder.load_string(KV)


for i in md_icons.keys():
	KV += f'''
			TooltipMDIconButton:
				icon: "{i}"
				tooltip_text: "{i}"
	'''
app().run()

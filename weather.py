from kivy.lang import Builder
from kivymd.app import MDApp
import json
from kivymd.uix.list import IconLeftWidget,TwoLineIconListItem
from kivymd.uix.card import MDCard

class MainApp(MDApp):
    title="Nuriddin's Weather App"
    
    def build(self):
        self.theme_cls.theme_style="Dark"
        self.theme_cls.material_style = "M3"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file("weather.kv")
    
    def on_start(self):
        with open('vils.json') as json_f:
            data_list=json.load(json_f)
        hudud_list=self.root.ids.hudud_list
        for item in data_list:
            line_item =TwoLineIconListItem(
                   IconLeftWidget(icon="office-building-marker"),
                    text=item['hudud_nomi'],
                    secondary_text=item['shahar_nomi']
            )
            hudud_list.add_widget(line_item)

MainApp().run()

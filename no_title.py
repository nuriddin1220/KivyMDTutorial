from kivy.config import Config
Config.set('graphics','position','custom')
Config.set('graphics','left',900)# from the left side of the screen
Config.set('graphics','top',200)

from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window




class MainApp(MDApp):
    def build(self):
        Window.borderless=True
        self.theme_cls.theme_style="Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file("no_title.kv")

MainApp().run()

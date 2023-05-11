from kivy.lang import Builder
from kivymd.app import MDApp



class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_pallette="Blue"
        self.theme_cls.accent_pallete="Red"
        return Builder.load_file("color_theme.kv")


MainApp().run()
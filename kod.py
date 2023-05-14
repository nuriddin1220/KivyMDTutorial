from kivy.lang import Builder
from kivymd.app import MDApp


class MainApp(MDApp):
    some_text="Hello, world!"
    def build(self):
        self.theme_cls.theme_style="Light"
        self.theme_cls.material_style = "M3"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file("kod.kv")

MainApp().run()

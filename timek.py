from kivy.lang import Builder
from kivymd.app import MDApp


class MainApp(MDApp):
    
    def build(self):
        self.theme_cls.theme_style="Light"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file("timek.kv")
    

    
MainApp().run()

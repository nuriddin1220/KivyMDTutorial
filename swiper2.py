from kivy.lang import Builder
from kivymd.app import MDApp


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style="Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file("swiper2.kv")
    def on_swipe_left(self):
        self.root.ids.toolbar.title="Swipe Left"
        print("You swipe left")
        
    def on_swipe_right(self):
        print("You swipe right")
        self.root.ids.toolbar.title="Swipe Right"
    
MainApp().run()

from kivy.lang import Builder
from kivymd.app import MDApp


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style="Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('list.kv')

    def presser(self,pressed,list_id):
        pressed.tertiary_text=f"You pressed {list_id}"
        
MainApp().run()

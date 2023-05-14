from kivy.lang import Builder
from kivymd.app import MDApp




class MainApp(MDApp):
    
    def callback_function(self,instance):
        self.root.ids.my_label.text=f"you pressed {instance.icon}"
        print(instance.icon)
    
    def open(self):
        self.root.ids.my_label.text=f"Open!"
    
    def close(self):
        self.root.ids.my_label.text=f"Close!"
    
    def build(self):
        self.data={
        "Python":["language-python","on_press", self.callback_function],
        "Ruby":["language-ruby","on_press", self.callback_function],
        "JavaScript":["language-javascript","on_press", self.callback_function]
        }
        self.theme_cls.theme_style="Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file("sd.kv")

MainApp().run()

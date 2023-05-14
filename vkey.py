from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.gridlayout import MDGridLayout
from kivy.uix.vkeyboard import VKeyboard

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style="Light"
        self.theme_cls.primary_palette = "BlueGray"
        
        layout=MDGridLayout(cols=1)
        self.label=MDLabel(text="Type Something",font_size="32")
        
        keyboard=VKeyboard(on_key_up=self.key_up,size_hint_x= 1)# when button released    
        layout.add_widget(self.label)
        layout.add_widget(keyboard)
        
        return layout
    
    
    def key_up(self,keyboard,keycode,*args):
        if isinstance(keycode,tuple):
            keycode=keycode[1]
        thing=self.label.text
        if thing=="Type Something":
            thing=''
        self.label.text=f'{thing}{keycode}'
                

MainApp().run()

from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.videoplayer import VideoPlayer

class MainApp(MDApp):
    title = "Simple Video Player"
    def build(self):
        self.theme_cls.theme_style="Dark"
        self.theme_cls.primary_palette = "BlueGray"
        
        player=VideoPlayer(source="api.mp4")
        
        #Assign player state
        player.state='play'
        player.options={'eos':'loop'}
        player.allow_stretch=True
        return player
        
MainApp().run()

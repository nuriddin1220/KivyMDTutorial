from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.pickers import MDDatePicker
from datetime import datetime, timedelta

class MainApp(MDApp):
    
    def build(self):
        self.theme_cls.theme_style="Light"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file("date.kv")
    
    #Click oK
    def on_save(self,instance,value,date_range):
        # print(instance,value,date_range)
        # self.root.ids.date_label.text=str(value)
        self.root.ids.date_label.text=str(date_range)
        
        
    def on_cancel(self,instance,value):
        self.root.ids.date_label.text="You Clicked the CANCEL"
    
    
    def show_date_picker(self):
        # date_dialog=MDDatePicker()# defuault current date
        # date_dialog=MDDatePicker(mode="range")--range
        # date_dialog=MDDatePicker(year=2022,month=12,day=20)# setting default date
        date_dialog = MDDatePicker( )
        date_dialog.bind(on_save=self.on_save,on_cancel=self.on_cancel)
        date_dialog.open()
    
MainApp().run()

from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
import json


class MainApp(MDApp):
    
    
    def build(self):
        with open('data.json') as json_data:
            data = json.load(json_data)
            data=[tuple(i.values()) for i in data]
            
        screen=Screen()
        table=MDDataTable(
            size_hint=(0.99, 0.7),
            check=True,
            use_pagination=True,
            pagination_menu_height='240dp',
            pagination_menu_pos="auto",
            background_color="#3734eb",
            background_color_header="#3734eb",
            background_color_selected_cell="#eb34c9",
            background_color_cell="#e3d1e0",
            rows_num=20,
            pos_hint= {'center_x': 0.5,'center_y': 0.5},
            column_data=[
                ("First Name",dp(30)),
                ("Last Name",dp(30)),
                ("Email Adress",dp(50)),
                ("Phone Number",dp(40))
            ],
            row_data=data
            # row_data=[(),().....]--values
        )
        
        table.bind(on_check_press=self.checked)
        table.bind(on_row_press=self.row_checked)
        
        self.theme_cls.theme_style="Light"
        self.theme_cls.primary_palette = "BlueGray"
        # return Builder.load_file("timek.kv")
        #add table to the screen
        screen.add_widget(table)
        return screen
    
    
    def checked(self, instance_table, current_row):
        print(instance_table,current_row)
    
    def row_checked(self, instance_table,instance_row):
        print(instance_table,instance_row)
    
MainApp().run()

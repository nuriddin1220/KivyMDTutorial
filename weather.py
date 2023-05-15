from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.list import IconLeftWidget,TwoLineIconListItem
from kivymd.uix.card import MDCard
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.image import Image
from kivymd.uix.label import MDIcon
from kivymd.uix.spinner.spinner import MDSpinner
from kivy.metrics import dp
from kivymd.uix.screen import MDScreen
import requests
import geocoder
import json


def get_current_location():
    g = geocoder.ip('me')
    if g.latlng:
        latitude, longitude = g.latlng
        return latitude, longitude
    else:
        return None

def get_weather(lat,long,appid,language='en'):
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'lat': lat,'lon': long,'appid': appid,'lang': language,'units': 'metric'}
    timeout_seconds = 5
    response = requests.get(url, params=params,timeout=timeout_seconds)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_icon(icon_code):
    url=f'https://openweathermap.org/img/wn/{icon_code}@2x.png'
    response = requests.get(url)
    return response.json()



class MainApp(MDApp):
    title="Nuriddin's Weather App"
    appid='a6ffc8b3cadf6c0445beba80ac186b62'
    spinner = None
    with open('vils.json') as json_f:
            data_list=json.load(json_f)

    def build(self):
        self.theme_cls.theme_style="Dark"
        self.theme_cls.material_style = "M3"
        self.theme_cls.primary_palette = "BlueGray"
        self.widget_added = False
        self.data_loaded = False
        self.spinner_status = False
        return Builder.load_file("weather.kv")
    
    def on_start(self):
        hudud_list=self.root.ids.hudud_list
        for item in self.data_list:
            line_item =TwoLineIconListItem(
                   IconLeftWidget(icon="office-building-marker"),
                    text=item['hudud_nomi'],
                    secondary_text=item['shahar_nomi']
            )
            hudud_list.add_widget(line_item)
        #REQUEST WEATHER STAFF


    def my_loc_tab(self):
        # spinner = self.root.ids.spinner_screen
        # my_location_card=self.root.ids.my_location_card
        # my_location_box=self.root.ids.my_location_box
        # my_location_box.remove_widget(my_location_card)
        # my_location_box.add_widget(self.root.ids.spinner_screen)
        # spinner.active=True
        data=get_current_location()
        # self.root.ids.my_spinner.active=False
        # if data is None:
        #     self.root.ids.my_location_box.remove_widget(self.root.ids.my_location_card)
        #     if  self.widget_added:
        #         pass
        #     else:
        #         self.widget_added=True
        #         self.root.ids.my_location_box.orientation='vertical'
        #         self.root.ids.my_location_box.add_widget(
        #            Image(source='no_weather_data.png',size_hint= (1, 0.8),pos_hint= {'center_x': 0.5})
        #            )
        #         self.root.ids.my_location_box.add_widget(
        #             MDLabel(
        #                 text="No Connection to the internet",
        #                 halign="center",
        #                 valign= 'center',
        #                 font_style="H5",
        #                 size_hint= (1, 0.2)
        #             ))
            
        # else:
        print(get_weather(data[0],data[1],self.appid))
        # my_location_box.remove_widget(spinner_screen)
        # my_location_box.add_widget(my_location_card)


MainApp().run()

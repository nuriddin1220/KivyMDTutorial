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
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
from kivy.uix.popup import Popup 
from kivy.uix.button import Button
import requests
import geocoder
import json


def get_current_location():
    g = geocoder.ip('me',timeout=5)
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
    with open('vils.json') as json_f:
            data_list=json.load(json_f)
    custom_loc=['00.0000','00.0000']

    def build(self):
        self.theme_cls.theme_style="Dark"
        self.theme_cls.material_style = "M3"
        self.theme_cls.primary_palette = "BlueGray"
        self.widget_added = False
        self.spinner_added=False
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

    def loc_released(self):
        geo_data=get_current_location()
        if geo_data is None:
            self.root.ids.network_error_label.opacity=1
            self.root.ids.network_error_label.text="Error:Getting GeoInfo data"
            self.root.ids.weather_button.disabled=True
        else:
            self.root.ids.weather_button.disabled=False
            self.root.ids.network_error_label.opacity=0
            self.root.ids.lat.text=f'Lat: {str(geo_data[0])}'
            self.root.ids.lon.text=f'Lon: {str(geo_data[1])}'
            self.custom_loc=[geo_data[0],geo_data[1]]
        self.root.ids.my_spinner.active=False


    def loc_pressed(self):
        self.root.ids.my_spinner.active=True

    def weather_pressed(self):
        self.root.ids.my_spinner.active=True

    def weather_released(self):
        if self.custom_loc[0]=="00.000":
            self.root.ids.weather_button.disabled=True
        else:
            weather_data=get_weather(self.custom_loc[0],self.custom_loc[1],self.appid)
            if weather_data is None:
                self.root.ids.network_error_label.opacity=1
                self.root.ids.network_error_label.text="Error:Getting Weather Info data"
                self.root.ids.weather_button.disabled=True
            print(weather_data)
            self.root.ids.my_spinner.active=False

    def my_loc_tab(self):
        pass



MainApp().run()

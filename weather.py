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
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.list.list import MDList
import datetime
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
    try:
        response = requests.get(url, params=params,timeout=timeout_seconds)
        return response.json()
    except:
        return None





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
        else:
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
            self.root.ids.network_error_label.text="Error:You need to take GeoInfo first"
        else:
            weather_data=get_weather(self.custom_loc[0],self.custom_loc[1],self.appid)
            print(weather_data)
            if weather_data is None:
                self.root.ids.network_error_label.opacity=1
                self.root.ids.network_error_label.text="Error:Getting Weather Info data"
            else:
                layout=MDCard(pos_hint={'center_x': 0.5,'center_y': 0.5},size_hint=(1,1),spacing=dp(5),padding=dp(5))
                #needed data
                icon_code=weather_data['weather'][0]['icon']
                icon_url=f'https://openweathermap.org/img/wn/{icon_code}@2x.png'
                description=weather_data['weather'][0]['description']
                temperature=weather_data['main']['temp']
                humidity=weather_data['main']['humidity']
                visibility=weather_data['visibility'] #m
                wind_speed=weather_data['wind']['speed'] #m/s
                clouds=weather_data['clouds']['all']
                city_name=weather_data['name']
                data_time=datetime.datetime.fromtimestamp(weather_data['dt']).strftime('%B %d, %Y %H:%M:%S')
                sunrise_time=datetime.datetime.fromtimestamp(weather_data['sys']['sunrise']).strftime('%B %d, %Y %H:%M:%S')
                sunset_time=datetime.datetime.fromtimestamp(weather_data['sys']['sunset']).strftime('%B %d, %Y %H:%M:%S')
                #showing data
                card1=MDCard(size_hint=(0.5,1),pos_hint={'center_x': 0.25,'center_y': 0.5},style="elevated")
                box1=MDGridLayout(cols=1,rows=2,padding=dp(10),spacing=dp(10))
                box1.add_widget(Image(source=icon_url,size_hint=(1,0.7)))
                box1.add_widget(MDLabel(text=f'DESCRIPTION : {description.upper()}',halign='center',size_hint=(1,0.3)))
                card1.add_widget(box1)
                layout.add_widget(card1)
                
                card2=MDCard(size_hint=(0.5,1),pos_hint={'center_x': 0.75,'center_y': 0.5},style="elevated")
                box2 =MDList()
                box2.add_widget(MDLabel(text='Weather Data',halign='center'))
                box2.add_widget(TwoLineIconListItem(IconLeftWidget(icon="temperature-celsius",theme_icon_color="Custom",icon_color="orange"),text=f"Temperature: {str(temperature)}",secondary_text= "Celsius"))
                box2.add_widget(TwoLineIconListItem(IconLeftWidget(icon="water-percent",theme_icon_color="Custom",icon_color="orange"),text=f"Humidity: {str(humidity)}",secondary_text= "Percent,%"))
                box2.add_widget(TwoLineIconListItem(IconLeftWidget(icon="eye",theme_icon_color="Custom",icon_color="orange"),text=f"Visibility: {str(visibility)}",secondary_text= "Meter"))
                box2.add_widget(TwoLineIconListItem(IconLeftWidget(icon="wind-power",theme_icon_color="Custom",icon_color="orange"),text=f"Wind speed: {str(wind_speed)}",secondary_text= "Meter/Sec"))
                box2.add_widget(TwoLineIconListItem(IconLeftWidget(icon="wind-power",theme_icon_color="Custom",icon_color="orange"),text=f"Cloudiness: {str(clouds)}",secondary_text= "Percent,%"))
                box2.add_widget(TwoLineIconListItem(IconLeftWidget(icon="city",theme_icon_color="Custom",icon_color="orange"),text=f"City name: {str(city_name)}",secondary_text= "name"))
                box2.add_widget(TwoLineIconListItem(IconLeftWidget(icon="clock-time-eight",theme_icon_color="Custom",icon_color="orange"),text=f"Data Time: {str(data_time)}",secondary_text= "human-readable"))
                box2.add_widget(TwoLineIconListItem(IconLeftWidget(icon="weather-sunset-up",theme_icon_color="Custom",icon_color="orange"),text=f"Sunrise Time: {str(sunrise_time)}",secondary_text= "human-readable"))
                box2.add_widget(TwoLineIconListItem(IconLeftWidget(icon="weather-sunset-down",theme_icon_color="Custom",icon_color="orange"),text=f"Sunset Time: {str(sunset_time)}",secondary_text= "human-readable"))
                
                card2.add_widget(MDScrollView(box2))
                layout.add_widget(card2)
                self.root.ids.my_location_screen.add_widget(layout)
            self.root.ids.my_spinner.active=False

    def my_loc_tab(self):
        pass



MainApp().run()

from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.list import IconLeftWidget,TwoLineIconListItem
from kivymd.uix.card import MDCard
from kivy.metrics import dp
from kivy.uix.popup import Popup
from kivymd.uix.button import MDFloatingActionButton
from kivy_garden.mapview import MapView ,MapMarker
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.list.list import MDList,OneLineAvatarIconListItem, IconLeftWidget,ImageLeftWidget
from kivy.uix.image import AsyncImage
from kivy.core.window import Window
import datetime
import requests
import geocoder
import json


def get_current_location():
    g = geocoder.ip('me')
    if g.latlng:
        latitude, longitude = g.latlng
        print(latitude,longitude)
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
    icon="weather-cloudy-clock"
    appid='a6ffc8b3cadf6c0445beba80ac186b62'
    with open('vils.json') as json_f:
            data_list=json.load(json_f)
    custom_loc=['00.0000','00.0000']
    data = {
        'REFRESH': 'refresh-circle',
        'RUSSIAN DESCRIPTION': 'translate',
        'LOCATION': 'map-marker-outline',
    }
    chosen_location=None

    def build(self):
        self.theme_cls.theme_style="Dark"
        self.theme_cls.material_style = "M3"
        self.theme_cls.primary_palette = "BlueGray"
        self.widget_added = False
        return Builder.load_file("weather.kv")
    
    
    
    def on_start(self):         
        hudud_list=self.root.ids.hudud_list
        for item in self.data_list:
            line_item =TwoLineIconListItem(
                   IconLeftWidget(icon="office-building-marker"),
                    text=item['hudud_nomi'],
                    secondary_text=item['shahar_nomi'],
                    on_release=lambda x, item=item: self.on_list_item_release(item)
            )
            hudud_list.add_widget(line_item)

    def author_button_released(self):
        menu = MDScrollView(
                            MDList(
                                OneLineAvatarIconListItem(IconLeftWidget(icon="account",theme_icon_color="Custom",icon_color="orange"),text=f"name: Sharipov Nuriddin"),
                                OneLineAvatarIconListItem(IconLeftWidget(icon="calendar-today-outline",theme_icon_color="Custom",icon_color="orange"),text=f"bith year: 1997"),
                                OneLineAvatarIconListItem(IconLeftWidget(icon="city",theme_icon_color="Custom",icon_color="orange"),text=f"from : Namangan"),
                                OneLineAvatarIconListItem(IconLeftWidget(icon="map-marker",theme_icon_color="Custom",icon_color="orange"),text=f"living location: Tashkent"),
                                OneLineAvatarIconListItem(IconLeftWidget(icon="briefcase-outline",theme_icon_color="Custom",icon_color="orange"),text=f"work: REPN JSC"),
                                OneLineAvatarIconListItem(IconLeftWidget(icon="bio",theme_icon_color="Custom",icon_color="orange"),text=f"bio: I am curious about testing Python libs")))
        popup = Popup(content=menu,title=f"Author",auto_dismiss=True,pos_hint = {'center_x':0.5,'top':0.9},size_hint=(0.5,0.5))
        popup.content=menu
        popup.open()
    
    def api_button_released(self):
        menu = MDScrollView(
                            MDList(
                                OneLineAvatarIconListItem(IconLeftWidget(icon="read",theme_icon_color="Custom",icon_color="orange"),text="""Current Weather Data API Call"""),
                                OneLineAvatarIconListItem(IconLeftWidget(icon="code-json",theme_icon_color="Custom",icon_color="orange"),text=f"formats: JSON, XML, and HTML formats"),
                                OneLineAvatarIconListItem(IconLeftWidget(icon="currency-usd-off",theme_icon_color="Custom",icon_color="orange"),text=f"options : Free and Paid subscriptions")))
        popup = Popup(content=menu,title=f"OpenWeather API",auto_dismiss=True,pos_hint = {'center_x':0.5,'top':0.9},size_hint=(0.6,0.7))
        popup.content=menu
        popup.open()


    def on_list_item_release(self,item):
        print(item)
        weather_data=get_weather(item['lat'],item['long'],self.appid)
        print(weather_data)
        if weather_data is not None:
            print(weather_data)
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
            menu = MDScrollView(
                            MDList(
                                OneLineAvatarIconListItem(ImageLeftWidget(source=icon_url),text=f"{description}"),
                                OneLineAvatarIconListItem(IconLeftWidget(icon="temperature-celsius",theme_icon_color="Custom",icon_color="orange"),text=f"Temperature: {str(temperature)} Celsius"),
                                OneLineAvatarIconListItem(IconLeftWidget(icon="water-percent",theme_icon_color="Custom",icon_color="orange"),text=f"Humidity: {str(humidity)} %"),
                                OneLineAvatarIconListItem(IconLeftWidget(icon="eye",theme_icon_color="Custom",icon_color="orange"),text=f"Visibility: {str(visibility)}"),
                                OneLineAvatarIconListItem(IconLeftWidget(icon="wind-power",theme_icon_color="Custom",icon_color="orange"),text=f"Wind speed: {str(wind_speed)} M/S"),
                                OneLineAvatarIconListItem(IconLeftWidget(icon="wind-power",theme_icon_color="Custom",icon_color="orange"),text=f"Cloudiness: {str(clouds)} %"),
                                OneLineAvatarIconListItem(IconLeftWidget(icon="city",theme_icon_color="Custom",icon_color="orange"),text=f"City name: {str(city_name)}"),
                                OneLineAvatarIconListItem(IconLeftWidget(icon="clock-time-eight",theme_icon_color="Custom",icon_color="orange"),text=f"Data Time: {str(data_time)}"),
                                OneLineAvatarIconListItem(IconLeftWidget(icon="weather-sunset-up",theme_icon_color="Custom",icon_color="orange"),text=f"Sunrise Time: {str(sunrise_time)}"),
                                OneLineAvatarIconListItem(IconLeftWidget(icon="weather-sunset-down",theme_icon_color="Custom",icon_color="orange"),text=f"Sunset Time: {str(sunset_time)}")))
            popup = Popup(content=menu,title=f"Information",auto_dismiss=True,pos_hint = {'center_x':0.5,'top':0.9},size_hint=(0.6,0.8))
            popup.content=menu
            popup.open()
        else:
            menu=MDLabel(text='Try Again:Network issue!',halign="center",size_hint=(1,1))
            popup = Popup(content=menu,title=f"Error",auto_dismiss=True,pos_hint = {'center_x':0.5,'center_y':0.5},size_hint=(0.4,0.2))
            popup.open()


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


    def loc_pressed(self):
        self.root.ids.network_error_label.opacity=1
        self.root.ids.network_error_label.text="Reading . . ."

    def back_to(self):
        self.root.ids.my_location_screen.add_widget(self.root.ids.my_location_screen)

    def weather_pressed(self):
        self.root.ids.network_error_label.opacity=1
        self.root.ids.network_error_label.text="Reading . . ."

    def weather_released(self):
        print(self.custom_loc)
        if self.custom_loc[0]=="00.0000":
            self.root.ids.network_error_label.text="Error:You need to take GeoInfo first"
        else:
            weather_data=get_weather(self.custom_loc[0],self.custom_loc[1],self.appid)
            print(weather_data)
            if weather_data is None:
                self.root.ids.network_error_label.opacity=1
                self.root.ids.network_error_label.text="Error:Getting Weather Info data"
            else:
                self.root.ids.network_error_label.opacity=0
                layout=MDCard(pos_hint={'center_x': 0.5,'center_y': 0.5},size_hint=(1,1),spacing=dp(5),padding=dp(5))
                #needed data
                icon_code=weather_data['weather'][0]['icon']
                icon_url=f'https://openweathermap.org/img/wn/{icon_code}@4x.png'
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
                box1=MDGridLayout(cols=1,rows=3,padding=dp(10),spacing=dp(10))
                refresh_button=MDFloatingActionButton(icon="close-circle",type='small',text_color="#211c29",theme_icon_color="Custom",on_release=lambda x: self.root.remove_widget(layout))
                refresh_button.bind(on_release=lambda x: self.root.ids.my_location_screen.remove_widget(layout))
                box1.add_widget(refresh_button)
                box1.add_widget(AsyncImage(source=icon_url,size_hint=(1,0.6),allow_stretch=True))
                box1.add_widget(MDLabel(text=f'DESCRIPTION : {description.upper()}',halign='center',size_hint=(1,0.2)))
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
            

    def my_loc_tab(self):
        self.root.ids.lat.text=f'Lat: {str(self.custom_loc[0])}'
        self.root.ids.lon.text=f'Lon: {str(self.custom_loc[1])}'
    
    def map_button_pressed(self):
        self.root.ids.map_label.text="Started . . ."
    
    def on_map_touch(self, instance, touch):
        if instance.collide_point(*touch.pos) and  touch.button == 'left':
            lat, lon = instance.get_latlon_at(touch.pos[0], touch.pos[1])
            lat,lon=round(lat,5),round(lon,5)
            self.chosen_location=[float(lat),float(lon)]
            print(f"Latitude: {lat}, Longitude: {lon}")   
            x = round((touch.x - instance.x) / instance.width,2)
            y = round((touch.y - instance.y) / instance.height,2)

            menu = MDScrollView(
                                MDList(
                                    OneLineAvatarIconListItem(
                                        IconLeftWidget(icon="map-marker-circle"),
                                        text=f"{str(lat)},{str(lon)}",
                                        # on_release=lambda x: print("Click!")
                                        ),
                                    OneLineAvatarIconListItem(
                                        IconLeftWidget(icon="information"),
                                         text="Get Weather Info",
                                        on_release=lambda x: self.call()
                                        )))
            popup = Popup(content=menu,title=f"Information",auto_dismiss=True,pos_hint = {'x':x,'top':y},size_hint=(0.38,0.3))
            popup.content=menu
            popup.open()

    def call(self):
        print('something to do')
        if self.chosen_location is not None:
            lat,lon=self.chosen_location[0],self.chosen_location[1]
            weather_data=get_weather(lat,lon,self.appid)
            if weather_data is not None:
                print(weather_data)
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
                menu = MDScrollView(
                                MDList(
                                    OneLineAvatarIconListItem(ImageLeftWidget(source=icon_url),text=f"{description}"),
                                    OneLineAvatarIconListItem(IconLeftWidget(icon="temperature-celsius",theme_icon_color="Custom",icon_color="orange"),text=f"Temperature: {str(temperature)} Celsius"),
                                    OneLineAvatarIconListItem(IconLeftWidget(icon="water-percent",theme_icon_color="Custom",icon_color="orange"),text=f"Humidity: {str(humidity)} %"),
                                    OneLineAvatarIconListItem(IconLeftWidget(icon="eye",theme_icon_color="Custom",icon_color="orange"),text=f"Visibility: {str(visibility)}"),
                                    OneLineAvatarIconListItem(IconLeftWidget(icon="wind-power",theme_icon_color="Custom",icon_color="orange"),text=f"Wind speed: {str(wind_speed)} M/S"),
                                    OneLineAvatarIconListItem(IconLeftWidget(icon="wind-power",theme_icon_color="Custom",icon_color="orange"),text=f"Cloudiness: {str(clouds)} %"),
                                    OneLineAvatarIconListItem(IconLeftWidget(icon="city",theme_icon_color="Custom",icon_color="orange"),text=f"City name: {str(city_name)}"),
                                    OneLineAvatarIconListItem(IconLeftWidget(icon="clock-time-eight",theme_icon_color="Custom",icon_color="orange"),text=f"Data Time: {str(data_time)}"),
                                    OneLineAvatarIconListItem(IconLeftWidget(icon="weather-sunset-up",theme_icon_color="Custom",icon_color="orange"),text=f"Sunrise Time: {str(sunrise_time)}"),
                                    OneLineAvatarIconListItem(IconLeftWidget(icon="weather-sunset-down",theme_icon_color="Custom",icon_color="orange"),text=f"Sunset Time: {str(sunset_time)}")))
                popup = Popup(content=menu,title=f"Information",auto_dismiss=True,pos_hint = {'center_x':0.5,'top':0.9},size_hint=(0.6,0.8))
                popup.content=menu
                popup.open()
            else:
                menu=MDLabel(text='Try Again:Network issue!',halign="center",size_hint=(1,1))
                popup = Popup(content=menu,title=f"Error",auto_dismiss=True,pos_hint = {'center_x':0.5,'center_y':0.5},size_hint=(0.4,0.2))
                popup.open()


    def map_button_released(self):
        geo_data=get_current_location()
        if geo_data is None:
            self.root.ids.map_label.text="Try Again:Getting GeoInfo data"
        else:
            self.root.ids.map_label.text="Creating Map . . ."
            self.custom_loc=[geo_data[0],geo_data[1]]
            try:
                mapview = MapView(zoom=11, lat=float(geo_data[0]), lon=float(geo_data[1]))
                mapview.bind(on_touch_down=self.on_map_touch)
                mapview.add_marker(MapMarker(lat=float(geo_data[0]), lon=(geo_data[1])))
                self.root.ids.map_screen.add_widget(mapview)
                # close_button=MDFloatingActionButton(icon="close-circle",type='small',text_color="#211c29",theme_icon_color="Custom",pos_hint={'right':0.99, 'top':0.99})
                # self.root.ids.map_screen.add_widget(close_button)
                # print(dir(mapview))
                self.root.ids.map_label.text=""
            except:
                self.root.ids.map_label.text="Try again! Map creation failed!"
                

MainApp().run()

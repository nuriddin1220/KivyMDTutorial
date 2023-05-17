from kivymd.app import MDApp
from kivy_garden.mapview import MapView 
class MapViewApp(MDApp):
    def build(self):
        mapview=MapView(
            zoom=10,
            lat=41.485344459189406,
            lon=69.0529400477957
        )
        return mapview
    
    
MapViewApp().run()
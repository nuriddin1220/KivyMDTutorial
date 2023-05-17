import geocoder
g = geocoder.ipinfo('me')
print(g.latlng)
print(g.city)
print(g.json)

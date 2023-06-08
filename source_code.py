#Importing Packages
import folium
from folium.features import CustomIcon
#Creating Map
mapObj = folium.Map(location=[28.00000000, 84.00000000], zoom_start=7)

#Styling Map
bordersStyle = {
    "color": "green",
    "weight": 2
}

folium.GeoJson("nepal-states.geojson", name="Nepal", style_function=lambda x: bordersStyle).add_to(mapObj)

#Creating dictionary
districts = [
    ("Kavrepalanchok", 27.498389, 85.532033),
    ("Dhading", 27.982826, 84.897179),
    ("Makwanpur", 27.442406, 85.117634),
    ("Nuwakot", 27.966667, 85.200000),
    ("Ramechhap", 27.331717, 86.054764),
    ("Sindhupalchok", 27.8122, 85.5218),
    ("Dolakha", 27.872688, 86.069912),
    ("Gorkha", 28.226633, 84.454245),
    ("Tanahun", 27.982056, 84.220363),
    ("Syangja", 28.106680, 83.880619),
    ("Palpa", 27.863889, 83.566389),
    ("Gulmi", 28.053161, 83.228654),
    ("Arghakhanchi", 27.894467, 83.045672),
    ("Khotang", 27.227429, 86.814718),
    ("Illam", 26.910079, 87.936897),
    ("Baitadi", 29.533576, 80.556167),
    ("Surkhet", 28.601789, 81.600906),
    ("Dhankuta", 26.98333,  87.33333)
]

# Add markers for each district
for district in districts:
    name, lat, lon = district
    custom_icon = CustomIcon(icon_image=r"C:\Users\hardi\OneDrive\Desktop\Map_Distribution_Monkey_Catastrophe\Custom_Marker.png", icon_size=(40,40))
    popup_content = f"<b>{name}</b>"
    folium.Marker([lat, lon], popup=popup_content, icon=custom_icon).add_to(mapObj)


mapObj.save("index.html")

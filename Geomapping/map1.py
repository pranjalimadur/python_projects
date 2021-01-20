import folium
import pandas

data = pandas.read_csv("Volcanoes.csv")
lat= list(data["y"])
lon= list(data["x"])
elev= list(data["ELEV"])

def color_marker(elevat):
    if elevat<1000:
        return 'green'
    elif 1000<=elevat<=3000:
        return 'orange'
    else:
        return 'red'

mp = folium.Map(location=[40.47,-88.93], zoom_start=6)

fgv=folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el)+" m", fill_color=color_marker(el),
    color = 'grey', fill_opacity=0.7))

#fg.add_child(folium.GeoJson(data= open('world.json','r', encoding='utf-8-sig'),
#style_function= lambda x: {'fillColor':'yellow' if x['properties']['POP2005'] < 1000000}))

fgp=folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data = open('world.json','r', encoding= 'utf-8-sig').read(),
style_function= lambda x:{'fillColor':'green' if x["properties"]["POP2005"] < 10000000
else 'orange' if 10000000 <= x["properties"]["POP2005"] < 30000000 else 'red' }))

mp.add_child(fgv)
mp.add_child(fgp)

mp.add_child(folium.LayerControl())

mp.save("Map1.html")

import folium
from folium.plugins import MiniMap, Geocoder
from estilos_map import estilos as st 
from manejo_datos import manejo_datos
class main():
    
    # abrimos el archivo que generata la capa de superficie de los tejados.
    
    ruta_geo = "D:\Mapa_Orcasitas\datos\Edificios_Orcasitas.json"
    # Crea el mapa y muestra el centro en las cordenadas indicadas.
    m = folium.Map(location=[40.36989654728313, -3.715546018233464], zoom_start= 15, tiles= None)
    #URLS de capas que se van a utilizar.
    url_ign = ("https://www.ign.es/wms-inspire/pnoa-ma")
    # Añade al mapa la capa del ing.
    ign_capa = folium.WmsTileLayer(url=url_ign,
                        name="Ortofoto PNOA",
                        fmt="image/png",
                        layers="OI.OrthoimageCoverage",
                        transparent=False,
                        attr="Instituto Geográfico Nacional").add_to(m)
    # Añade un minimapa.
    tiles = folium.TileLayer( tiles='http://services.arcgisonline.com/arcgis/rest/services/World_Imagery/MapServer', attr='Map tiles by Esri, DigitalGlobe, GeoEye, i-cubed, USDA FSA, USGS, AEX, Getmapping, Aerogrid, IGN, IGP, swisstopo, and the GIS User Community'
 )
    mini_map = MiniMap(tile_layer= tiles).add_to(m)
 
    #Añade una capa que muestra la superficie de los tejagidos dependiendo de de los metros.
    folium.GeoJson(data= ruta_geo,
                   style_function= st.superficie,
                   name= "Superficie disponible m\u00B2").add_to(m)
    #Añade el control de capas.
    Geocoder().add_to(m)
    folium.LayerControl().add_to(m)
    
    m.save(".\public_html\index_orcasitas.html")
if __name__ == "__main__":
    main()
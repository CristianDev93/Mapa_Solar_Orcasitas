
"""En esta clase se declaran metodos que se utilizaran para dar color a las capas obtenidas de
archivos geojson"""
class estilos:
    
    def __init__(self):
        pass
    # Metodo que da estilo segun la el nivel de radiacion solar anual.
    def irradiacion(feature):
        rad = feature["properties"]["Radiacion_KWh_m2_Anual"]
        if rad < 250:
            return {'fillColor': '#6B73FD', 'color': '#6B73FD', 'fillOpacity': 1.0}
        elif rad < 500:
            return {'fillColor': '#3ACEFE', 'color': '#3ACEFE', 'fillOpacity': 1.0}
        elif rad < 750:
            return {'fillColor': '#89F0CC', 'color': '#89F0CC', 'fillOpacity': 1.0}
        elif rad < 1000:
            return {'fillColor': '#B4FD77', 'color': '#B4FD77', 'fillOpacity': 1.0}
        elif rad < 1250:
            return {'fillColor': '#FFFF73', 'color': '#FFFF73', 'fillOpacity': 1.0}
        elif rad < 1500:
            return {'fillColor': '#F8DD1C', 'color': '#F8DD1C', 'fillOpacity': 1.0}
        elif rad < 1750:
            return {'fillColor': '#FF9A0B', 'color': '#FF9A0B', 'fillOpacity': 1.0}
        elif rad < 2020:
            return {'fillColor': '#FE230A', 'color': '#FE230A', 'fillOpacity': 1.0}
        else:
            return {'fillColor': '#FFFFFF', 'color': '#FFFFFF', 'fillOpacity': 1.0}
    # Metodo que da color a los poligonos, segun la superficie disponible.  
    def superficie(feature):
        """Aplica un estilo según la superficie disponible o datos de irradiación."""
        superficie = feature['properties'].get('Tejado_Disponible_m2', 0)
        if superficie in range(0, 21):
            return {'fillColor': '#FFFFB2', 'color': '#FFFFB2', 'weight': 2, 'fillOpacity': 0.7}
        elif superficie in range(20, 81):
            return {'fillColor': '#FECC5C', 'color': '#FECC5C', 'weight': 2, 'fillOpacity': 0.7}
        elif superficie in range(80, 401):
            return {'fillColor': '#FD8D3C', 'color': '#FD8D3C', 'weight': 2, 'fillOpacity': 0.7}
        elif superficie in range(400, 801):
            return {'fillColor': '#F03B20', 'color': '#F03B20', 'weight': 2, 'fillOpacity': 0.7}
        elif superficie in range(800, 1604):
            return {'fillColor': '#BD0026', 'color': '#BD0026', 'weight': 2, 'fillOpacity': 0.7}
        else:
            return {'fillColor': '#FFFFFF', 'color': '#000000', 'weight': 2, 'fillOpacity': 0.7}
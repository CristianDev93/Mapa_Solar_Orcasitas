import json
import tkinter as tk
from shapely.geometry import shape, mapping
from shapely.ops import transform
from tkinter import filedialog
import fiona


"""Clase donde se definen metodós para realizar operaciones sobre los archivos"""
class manejo_datos():
    root = tk.Tk()
    root.withdraw()

    # TODO: función que seleccionando un geojson simplilfica las cordenadas, quitandole decimales para facililtar su manejo.
    def redondear_coordenadas():
        
        f = filedialog.askopenfilename()
        
        with open(f, "r") as file:
            
            dat = json.load(file)
        
        #Recorre el archivo quitando decimales a las cordenadas.
        for feature in dat["features"]:
            geom = feature["geometry"]
            if geom["type"] == "Point":
                geom["coordinates"] = [round(coord, 4) for coord in geom["coordinates"]]
            elif geom["type"] in ["LineString", "MultiPoint"]:
                geom["coordinates"] = [[round(coord, 4) for coord in point] for point in geom["coordinates"]]
            elif geom["type"] == "Polygon":
                geom["coordinates"] = [[[round(coord, 4) for coord in point] for point in ring] for ring in geom["coordinates"]]
        nf = filedialog.asksaveasfilename(defaultextension= "Irradiacion_simpificado.geojson",)
        
        with open(nf , "w") as f:
            json.dump(dat, f)
            
    # TODO: Función para  simplificar la geometria, elimina los puntos redundantes y vaja ala definición.
    def simplificar_geo():

        tolerancia = 0.01
        f = filedialog.askopenfile()
        nf = filedialog.asksaveasfilename(defaultextension= "Irradiacion_final.geojson",)
        
        with fiona.open(f) as src:
            with fiona.open(nf, "w", **src.meta) as dst:
                for feature in src:
                    geom = shape(feature["geometry"])
                    simpli_geom = geom.simplify(tolerancia)
                    feature["geometry"] = mapping(simpli_geom)
                    dst.write(feature)
            
        
        
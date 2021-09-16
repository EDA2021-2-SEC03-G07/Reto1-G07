"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


from Test.bst.test_bst import cmpfunction
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as insert
from DISClib.Algorithms.Sorting import quicksort as quick
from DISClib.Algorithms.Sorting import mergesort as merge
from datetime import date, datetime, timedelta
assert cf
import time
# Construccion de modelos

def newCatalog(Dataestructure):
    
    catalog = {'Artist': None,
               'Artwork': None}

    catalog['Artist'] = lt.newList(Dataestructure)
    catalog['Artwork'] = lt.newList(Dataestructure,cmpfunction=cmpArtworkByDateAcquired)
    #print("SOY UN "+Dataestructure)
    return catalog

# Funciones para agregar informacion al catalogo

def addArtist(catalog, artist):
    lt.addLast(catalog["Artist"],artist)    

def addArtwork(catalog,artwork):
    if artwork["DateAcquired"] == "":
        artwork["DateAcquired"] = "1800-01-01"
    lt.addLast(catalog["Artwork"],artwork)

# Funciones para creacion de datos

def newArtist():
    Artist = {}
    return Artist

def newArtwork():
    Artwork = {}
    return Artwork

# Funciones de consulta

def last3elemts(catalog):
    #Lo hice así porque me estresé con el while que me estaba arrojando un montón de errores.
    #Para la siguiente entrega lo tengo arreglado :D
    lasts_artists = []
    last_artworks = []
    lasts_artists.append(lt.lastElement(catalog["Artist"]))
    lt.removeLast(catalog["Artist"])
    lasts_artists.append(lt.lastElement(catalog["Artist"]))
    lt.removeLast(catalog["Artist"])
    lasts_artists.append(lt.lastElement(catalog["Artist"]))
    #Obras de arte 
    last_artworks.append(lt.lastElement(catalog["Artwork"]))
    lt.removeLast(catalog["Artwork"])
    last_artworks.append(lt.lastElement(catalog["Artwork"]))
    lt.removeLast(catalog["Artwork"])
    last_artworks.append(lt.lastElement(catalog["Artwork"]))
    print("Artistas: ", lasts_artists)
    print("")
    print("Obras de arte: ",last_artworks )
    # return lasts_artists
    # Se cargan como año/mes/día
    # fecha1= time.strptime(catalog['Artwork']['elements'][2]['DateAcquired'], "%Y-%m-%d")
    # fecha2 = time.strptime(catalog['Artwork']['elements'][0]['DateAcquired'], "%Y-%m-%d")
    # if fecha1 > fecha2:
    #     print("Fecha1 es menor!")
    # else:
    #     print("Fecha2 es mayor!")
    #Si funciona! ;3
# Funciones utilizadas para comparar elementos dentro de una lista
def cmpArtworkByDateAcquired(artwork1, artwork2):
    #Preguntar aquí cómo es que salen los elementos artwork1/2
    #I mean, cuáles son las keys que tienen para poder hacer la comparación
    #De manera correcta y eficiente.
    date1 = time.strptime(artwork1['DateAcquired'], "%Y-%m-%d")
    date2 = time.strptime(artwork2['DateAcquired'], "%Y-%m-%d")
    return date1 < date2

#Funciones de ordenamiento
def order_artworks(catalog, size, TypeofOrder):
    #Preguntar por qué está arrojando error esta función
    #Aunque probablemente sea porque no se está cargando bien el cmpfunction
    sb_list = lt.subList(catalog["Artwork"], 1, size)
    sb_list = sb_list.copy()
    sorted_lt = None
    start = time.process_time()
    if TypeofOrder == 1:
        sorted_lt = sa.sort(sb_list, cmpArtworkByDateAcquired)
    if TypeofOrder == 2:
        sorted_lt = insert.sort(sb_list, cmpArtworkByDateAcquired)
    if TypeofOrder == 3:
        sorted_lt = quick.sort(sb_list, cmpArtworkByDateAcquired)
    if TypeofOrder == 4:
        sorted_lt = merge.sort(sb_list, cmpArtworkByDateAcquired)
    end = time.process_time()
    print("El tiempo fue: ")
    time_mseg = (end - start)*1000
    return time_mseg, lt.size(sorted_lt)
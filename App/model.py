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


from typing import OrderedDict
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
from collections import OrderedDict

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
    if artist["Nationality"] == "":
        artist["Nationality"]= "Unknown"
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

'''def last3elemts(catalog):
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
    #Si funciona! ;3'''

def last3elements(catalog):
    last_artists = []
    last_artworks = []
    for i in range(-3,0):
        last_artists.append(catalog["Artist"]["elements"][i])
        last_artworks.append(catalog["Artwork"]["elements"][i])
    print(last_artists)
    print(last_artworks)

def firstelement(catalog):
    first_artist= lt.firstElement(catalog["Artist"])
    first_artwork= lt.firstElement(catalog["Artwork"])
    print(first_artist)
    print(first_artwork)

def last3elements_universal(catalog):
    last_artworks = []
    for i in range(-3,0):
        last_artworks.append(catalog["elements"][i])
    print(last_artworks)

def firstelements_universal(catalog):
    first_artworks = []
    for i in range(0,3):
        first_artworks.append(catalog["elements"][i])
    print(first_artworks)

# Funciones utilizadas para comparar elementos dentro de una lista
def cmpArtworkByDateAcquired(artwork1, artwork2):
    date1 = time.strptime(artwork1['DateAcquired'], "%Y-%m-%d")
    date2 = time.strptime(artwork2['DateAcquired'], "%Y-%m-%d")
    return date1 < date2

#Funciones de ordenamiento
def order_artworks(catalog):
    '''sb_list = lt.subList(catalog["Artwork"], 1, size)
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
    time_mseg = (end - start)*1000
    return time_mseg, sorted_lt'''
    copia_catalogo= catalog["Artwork"].copy()
    ordered_list= merge.sort(copia_catalogo, cmpArtworkByDateAcquired)
    return ordered_list


# requerimiento 2

def artworks_in_range(catalog, inicial, final):
    fechaini= time.strptime(inicial,"%Y-%m-%d")
    fechafina= time.strptime(final,"%Y-%m-%d")
    listix= lt.newList("ARRAY_LIST")
    artwork_elements= catalog["elements"]
    for element in range(0,lt.size(catalog)):
        if time.strptime(artwork_elements[element]["DateAcquired"], "%Y-%m-%d") >= fechaini and time.strptime(artwork_elements[element]["DateAcquired"], "%Y-%m-%d") <= fechafina:
            lt.addLast(listix,artwork_elements[element])
    return listix

def countpurchased(catalog):
    artwork_elements= catalog["elements"]
    cont= 0
    for element in artwork_elements:
        if element["CreditLine"].lower().find("purchase") >= 0:
            cont+= 1
    return cont

# requerimiento 3
def artworks_by_artist(catalog, nombre):
    artist_elements= catalog["Artist"]["elements"]
    for element in artist_elements:
        if element["DisplayName"] == nombre:
            id= element["ConstituentID"]

    artwork_elements= catalog["Artwork"]["elements"]
    listix= lt.newList("ARRAY_LIST")
    for element in artwork_elements:
        if element["ConstituentID"].find(id) >= 0:
            lt.addLast(listix,element)

    return listix, id, lt.size(listix)

def techniquesxartist(catalog):
    dict_techniques= {}
    for element in catalog["elements"]:
        if element["Medium"] not in dict_techniques.keys():
            #lt.addLast(lista_techniques,[element["Medium"],1])
            #lista_techniques["elements"][element["Medium"]]= 1
            dict_techniques[element["Medium"]]= 1
        else:
            dict_techniques[element["Medium"]]+= 1
    
    totaltecnicas= len(dict_techniques)

    toptechnique= max(dict_techniques,key=dict_techniques.get)
    obrastoptechnique= max(dict_techniques.values())

    return totaltecnicas, toptechnique, obrastoptechnique

def obrascontecnica(catalog,tecnica):
    artist_elements= catalog["elements"]
    listix= lt.newList("ARRAY_LIST")
    for element in artist_elements:
        if element["Medium"] == tecnica:
            lt.addLast(listix,element)
    
    return listix


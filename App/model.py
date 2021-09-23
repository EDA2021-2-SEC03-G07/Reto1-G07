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


import config as cf
import re
from DISClib.DataStructures.arraylist import getElement, lastElement, size
from Test.bst.test_bst import cmpfunction
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as insert
from DISClib.Algorithms.Sorting import quicksort as quick
from DISClib.Algorithms.Sorting import mergesort as merge
from datetime import date, datetime, timedelta
assert cf
import time
import operator
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

def first_last3elemts(lista):
    first_list = lt.newList('ARRAY_LIST')
    last_list = lt.newList('ARRAY_LIST')
    for i in range(-3,0):
        x = lt.getElement(lista,i)
        lt.addLast(last_list, x)
    for j in range(0,3):
        x = lt.getElement(lista,j)
        lt.addLast(first_list, x)
    print("Los primeros son: ", first_list)
    print("Los últimos son: ", last_list)

def Requerimiento_1(catalog, rango_min, rango_max):
    listica = catalog['Artist']['elements']
    lista_ordenada = lt.newList('ARRAY_LIST')
    for data in listica:
        if int(data['BeginDate']) > rango_min and int(data['BeginDate']) < rango_max:
            diccionario = {}
            diccionario['DisplayName'] = data['DisplayName']
            diccionario['BeginDate'] = data['BeginDate']
            diccionario['EndDate'] = data['EndDate']
            diccionario['Nationality'] = data['Nationality']
            diccionario['Gender'] = data['Gender']
            lt.addLast(lista_ordenada, diccionario)
    lista_sorted = lt.subList(lista_ordenada, 1, len(lista_ordenada))
    lista_sorted = lista_sorted.copy()
    final_sort = merge.sort(lista_ordenada, cmpArtistbyYear)
    #print(size(final_sort))
    return final_sort

def Requerimiento_4(catalog):
    #Puedo usar el ConstituentID de artist y artworks para relacionar las obras y artistas
    #Organizar primero los ID para luego comparar ID de Artwork y ID de Artist
    artworks = catalog['Artwork']
    artist = catalog['Artist']
    dict_countrys = {}
    dict_top = {}
    mini_dic = {}
    sort_IdArtist = lt.subList(artist,1,size(artist))
    sort_IdArtwork = lt.subList(artworks,1,size(artworks))
    sort_IdArtist = sort_IdArtist.copy()
    sort_IdArtwork = sort_IdArtwork.copy()
    sorted_artist = merge.sort(sort_IdArtist, cmpByConstituentID)
    sorted_artwork = merge.sort(sort_IdArtwork, cmpByConstituentID)
    #Organicé los constituent ID para que se comparen de forma más rápida
    for i in sorted_artist['elements']:
        a = i['ConstituentID']
        for j in sorted_artwork['elements']:
            b = j['ConstituentID']
            if a in b:
                mini_dic = {}
                mini_dic['Title'] = j['Title']
                mini_dic['DisplayName'] = i['DisplayName']
                mini_dic['Date'] = j['Date']
                mini_dic['Medium'] = j['Medium']
                mini_dic['Dimensions'] = j['Dimensions']
                #print(mini_dic)
                #EN LA LLAVE DE LA NACIONALIDAD, HACER UN COUNTLIST PARA VER EL TOP
                if i['Nationality'] in dict_countrys:
                    lt.addLast(dict_countrys[i['Nationality']],mini_dic)
                    dict_top[i['Nationality']] = size(dict_countrys[i['Nationality']])
                if i['Nationality'] not in dict_countrys:
                    dict_countrys[i['Nationality']] = lt.newList('ARRAY_LIST')
                    dict_top[i['Nationality']] = lt.newList('ARRAY_LIST')
                    lt.addLast(dict_countrys[i['Nationality']],mini_dic)
    sortedDict_top = sorted(dict_top.items(), key=operator.itemgetter(1))
    país_top = lt.newList('ARRAY_LIST')
    for k in range(0,11):
        for top in sortedDict_top:
            lt.addLast(país_top,top)
    return país_top

# Funciones utilizadas para comparar elementos dentro de una lista
def cmpArtworkByDateAcquired(artwork1, artwork2):
    #Preguntar aquí cómo es que salen los elementos artwork1/2
    #I mean, cuáles son las keys que tienen para poder hacer la comparación
    #De manera correcta y eficiente.
    date1 = time.strptime(artwork1['DateAcquired'], "%Y-%m-%d")
    date2 = time.strptime(artwork2['DateAcquired'], "%Y-%m-%d")
    return date1 < date2

def cmpArtistbyYear(artist1, artist2):
    return int(artist1['BeginDate']) < int(artist2['BeginDate'])

def cmpByConstituentID(ID1,ID2):
    id1 = re.sub("\[,\]", "", ID1['ConstituentID'])
    id2 = re.sub("\[,\]", "", ID2['ConstituentID'])
    return id1 < id2

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
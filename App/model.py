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
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

# Construccion de modelos

def newCatalog():
    
    catalog = {'Artist': None,
               'Artwork': None,}

    catalog['Artist'] = lt.newList('SINGED_LINKED')
    catalog['Artwork'] = lt.newList('SINGED_LINKED')
    return catalog

# Funciones para agregar informacion al catalogo

def addArtist(catalog, artist):
    lt.addLast(catalog["Artist"],artist)    

def addArtwork(catalog,artwork):
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
    return lasts_artists

# Funciones utilizadas para comparar elementos dentro de una lista

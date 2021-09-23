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
 """

from App.model import artworks_by_artist, cmpArtworkByDateAcquired, last3elements
import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initCatalog(Dataestructure):
    catalog = model.newCatalog(Dataestructure)
    return catalog

# Funciones para la carga de datos

def loadData(catalog):
    loadArtist(catalog)
    loadArtworks(catalog)

def loadArtist(catalog):

    Artistfile = cf.data_dir + 'Artists-utf8-80pct.csv'
    input_file = csv.DictReader(open(Artistfile, encoding='utf-8'))
    for Artist in input_file:
        model.addArtist(catalog, Artist)


def loadArtworks(catalog):
    Artworks = cf.data_dir + 'Artworks-utf8-80pct.csv'
    input_file = csv.DictReader(open(Artworks, encoding='utf-8'))
    for Artwork in input_file:
        model.addArtwork(catalog, Artwork)

#Funciones de print
def PrintResults(lista):
    printing = model.first_last3elemts(lista)
    return printing
#Funciones de consulta

def loadLast3elements(catalog):
    last3 = model.last3elements(catalog)
    return last3

def loadfirstelement(catalog):
    first= model.firstelement(catalog)
    return first

def loadLast3_universal(catalog):
    last3= model.last3elements_universal(catalog)
    return last3

def loadFirst_universal(catalog):
    first= model.firstelements_universal(catalog)
    return first
#Requerimiento 1
def Requerimiento_1(catalog, rango_min, rango_max):
    req1 = model.Requerimiento_1(catalog, rango_min, rango_max)
    return req1
# requerimiento 2

def ordered_lists(catalog):
    order_lt = model.order_artworks(catalog)
    return order_lt

def load_artworks_in_range(catalog,inicial,final):
    artworks= model.artworks_in_range(catalog,inicial,final)
    return artworks

def countpurchased(catalog):
    num= model.countpurchased(catalog)
    return num

# requerimiento 3

def artworks_by_artist(catalog, nombre):
    list= model.artworks_by_artist(catalog,nombre)
    return list[0]

def artworks_by_artist_size(catalog, nombre):
    info= model.artworks_by_artist(catalog,nombre)
    return info[2]

def artist_id(catalog, nombre):
    info= model.artworks_by_artist(catalog,nombre)
    return info[1]

def numtechniquesxartist(catalog):
    techniques= model.techniquesxartist(catalog)
    return techniques[0]

def tecnicamasusada(catalog):
    techniques= model.techniquesxartist(catalog)
    return techniques[1]

def obrascontecnicamasusada(catalog):
    techniques= model.techniquesxartist(catalog)
    return techniques[2]

def obrascontecnica(catalog,tecnica):
    obras= model.obrascontecnica(catalog,tecnica)
    return obras
#Requerimiento 4
def Requerimiento_4(catalog):
    req_4 = model.Requerimiento_4(catalog)
    return req_4
﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import config as cf
import sys
import controller
default_limit = 1000
sys.setrecursionlimit(default_limit*10)

from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def initCatalog(Dataestructure):
    """
    Inicializa el catalogo
    """
    return controller.initCatalog(Dataestructure)

def loadData(catalog):
    """
    Carga los datos en la estructura de datos
    """
    controller.loadData(catalog)

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar cronológicamente los artistas")
    print("3- Listar cronológicamente las adquisiciones")
    print("4- Clasificar las obras de un artista por técnica")
    print("5- Clasificar las obras por la nacionalidad de sus creadores")
    print("6- Transportar obras de un departamento")
    print("7- Proponer una nueva exposición en el museo")

def PrintResults(ord_list, sample=10):
    

    pass

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("\nIngrese la estructura de datos que desea")
        print("1) ARRAY_LIST\t2) SINGLE_LINKED")
        Option = input("Digite el número de la opción que desea: ")
        if int(Option) == 1:
            Dataestructure = "ARRAY_LIST"
            #print(Dataestructure)
        elif int(Option) == 2:
            Dataestructure = "SINGLE_LINKED"
            #print(Dataestructure)
        catalog = initCatalog(Dataestructure)
        loadData(catalog)
        print("Se cargaron exitosamente los datos")
        print("Aritistas cargados: "+ str(lt.size(catalog["Artist"])))
        print("Obras cargadas: "+ str(lt.size(catalog["Artwork"])))

    elif int(inputs[0]) == 2:
        rango_min = int(input("Ingrese la fecha mínima: "))
        rango_max = int(input("Ingrese la fecha máxima: "))
        sort_list = controller.Requerimiento_1(catalog, rango_min, rango_max)
        print(controller.PrintResults(sort_list))

    elif int(inputs[0]) == 3:
        size = int(input("Indique el tamaño de la muestra: "))
        TypeofOrder = int(input("\nIndique el tipo de ordenamiento:"
                            " 1) Shell Sort 2) Insertion Sort 3) Quick Sort 4) Merge Sort\n"))
        tiempo,lista =controller.ordered_lists(catalog, size, TypeofOrder)
        print(tiempo)
        print(lista)

    elif int(inputs[0]) == 5:
        final = controller.Requerimiento_4(catalog)
    else:
        sys.exit(0)
sys.exit(0)
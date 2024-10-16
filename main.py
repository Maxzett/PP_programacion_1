
from paquete.funciones import * 
'''
con 3 depósitos distribuidos en diferentes
provincias (PBA, Jujuy y Neuquén).
Los depósitos pueden almacenar 7 tipos diferentes de artículos: químicos, trapos, escobas,
cepillos, papel higiénico, jabón y pañuelos descartables.'''

lista_depositos = ['pba', 'jujuy', 'neuquen']
lista_articulos = ['quimicos', 'trapos', 'escobas', 'cepillos', 'papel higienico', 'jabon', 'pañuelos']

'''1. Obtener existencias: para ello deberá cargar en el main la existencia de cada artículo
en todos los depósitos. En una lista de cantidad, no uno por uno. Por lo que habrá una
matriz con 3 columnas o filas, provincia, tipo de artículo y cantidad.'''

planilla_datos = []
lista_cantidad_total = []

def cargar_existencias(matriz: list) -> list:
    
    lista_cant_pba = []
    lista_cant_jujuy = []
    lista_cant_neuquen = []

    for depositos in range(len(lista_depositos)):
        deposito = input('Ingrese el deposito: ')

        for articulos in range(len(lista_articulos)):
            cantidad = input(f'Ingrese la cantidad de {lista_articulos[articulos]}: ')
            
            if deposito == 'pba':
                lista_cant_pba += cantidad
            elif deposito == 'jujuy':
                lista_cant_jujuy += cantidad
            else:
                lista_cant_neuquen += cantidad
    
    
    lista_cantidad_total = lista_cant_pba , lista_cant_jujuy , lista_cant_neuquen
    print(lista_cantidad_total)
    
    
    return matriz
        

cargar_existencias(lista_cantidad_total)

print(calcular_total_por_fila(lista_cantidad_total))
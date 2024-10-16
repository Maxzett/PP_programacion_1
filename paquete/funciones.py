 
'''
2. Calcular por cada depósito la cantidad total de artículos almacenados entre todos los
tipos.
'''

def calcular_total_por_fila(matriz: list) -> list:
    
    for i in range(len(matriz)):
        
        for j in range(i, len(matriz) - 1):
            
            if i == matriz[i]:
                matriz[i] += j             
            elif i == matriz[i+1]:
                matriz[i+1] += j
            else:
                matriz[i+2] += j

    return matriz
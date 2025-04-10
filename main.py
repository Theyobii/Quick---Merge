import random
import time
from typing import List, Dict
import os
os.system("clear")

# Generar datos aleatorios para CarFix
def generar_carros(n: int) -> List[Dict]: 
    carros = []
    tipos_servicio = ["Frenos", "Motor", "Electrónica", "Transmisión", "Llantas"]
    tipos_carro = ["Toyota", "Mitsubishi", "Yari", "Terio", "Aveo", "Ford", "Chevrolet", "Turpial"]
    for i in range(n):
        carros.append({
            "ID": i + 1,
            "Prioridad": random.randint(1, 3),
            "Tiempo": random.randint(30, 240),
            "Servicio": random.choice(tipos_servicio),
            "tipo": random.choice(tipos_carro)
        })
    return carros

# Algoritmo Merge Sort
def merge_sort(carros: List[Dict]) -> List[Dict]:
    if len(carros) <= 1:
        return carros
    mitad = len(carros) // 2
    derecho = merge_sort(carros[:mitad])
    izquierdo = merge_sort(carros[mitad:])
    return merge(derecho, izquierdo)

def merge(izquierdo: List[Dict], derecho: List[Dict]) -> List[Dict]:
    resultado = []
    i = j = 0
    while i < len(izquierdo) and j < len(derecho): # Ordenar por Prioridad y luego por Tiempo
        if derecho[i]["Prioridad"] < derecho[j]["Prioridad"] or \
           (derecho[i]["Prioridad"] == derecho[j]["Prioridad"] and izquierdo[i]["Tiempo"] < derecho[j]["Tiempo"]):
            resultado.append(izquierdo[i])
            i += 1
        else:
            resultado.append(derecho[j])
            j += 1
    resultado.extend(izquierdo[i:])
    resultado.extend(derecho[j:])
    return resultado

# Algoritmo Quick Sort
def quick_sort(carros: List[Dict]) -> List[Dict]:
    if len(carros) <= 1:
        return carros
    pivote = carros[len(carros) // 2]
    izquierdo = [v for v in carros if (v["Prioridad"] < pivote["Prioridad"]) or 
           (v["Prioridad"] == pivote["Prioridad"] and v["Tiempo"] < pivote["Tiempo"])]
    mitad = [v for v in carros if v == pivote]
    derecho = [v for v in carros if (v["Prioridad"] > pivote["Prioridad"]) or 
            (v["Prioridad"] == pivote["Prioridad"] and v["Tiempo"] > pivote["Tiempo"])]
    return quick_sort(izquierdo) + mitad + quick_sort(derecho)

# Comparación de rendimiento
def comparar_rendimiento(carros: List[Dict]):
    algoritmos = {
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort   
    }
    resultados = {}
    for nombre, algoritmo in algoritmos.items():
        copia_carros = carros.copy()
        inicio = time.time()
        ordenados = algoritmo(copia_carros)
        tiempo = time.time() - inicio
        resultados[nombre] = {
            "Tiempo": tiempo,
            "Primeros 3": ordenados[:10]
        }
    return resultados

# inicio
if __name__ == "__main__":
    carros = generar_carros(3000)  # Prueba de 3000 vehículos
    resultados = comparar_rendimiento(carros)
    
    print("=== CarFix===")
    for algo, datos in resultados.items():
        print(f"\n**{algo}**:")
        print(f"  - Tiempo: {datos['Tiempo']:.5f} segundos")
        print("  - Vehículos prioritarios:")
        for v in datos["Primeros 3"]:
            print(f"    ID: {v['ID']}, Tipo: {v['tipo']}, Prioridad: {v['Prioridad']}, Tiempo: {v['Tiempo']} min, Servicio: {v['Servicio']}")

import re
from collections import Counter

def frase_counter():
    with open('contenidos_readmes.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    frases = []
    
    for i in range(1, len(lines), 2):  # Las frases están en las líneas impares
        frase = lines[i].strip()  # Limpiar espacios y saltos de línea
        if frase:  # Solo agregar si la frase no está vacía
            frases.append(frase)
    
    counter = Counter(frases)
    
    for frase, times in counter.items():
        print(f'"{frase}" se repite {times} vez/veces.')

frase_counter()

import random

def generar_quiniela(num_partidos):
    resultados = []
    opciones = ['1', 'X', '2']
    
    for _ in range(num_partidos):
        resultado = random.choice(opciones)
        resultados.append(resultado)
    
    return resultados

def imprimir_quiniela(resultados):
    print("Quiniela de fútbol:")
    for i, resultado in enumerate(resultados, 1):
        print(f"Partido {i}: {resultado}")

if __name__ == "__main__":
    num_partidos = 15  # Número típico de partidos en una quiniela de fútbol
    quiniela = generar_quiniela(num_partidos)
    imprimir_quiniela(quiniela)
